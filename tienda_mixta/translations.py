"""
Módulo de traducciones personalizadas para Tienda Mixta La 40
Corrige traducciones problemáticas del sistema Frappe/ERPNext y aplica traducciones faltantes
"""

import frappe
import csv
import os
from frappe import _

def get_translations():
    """
    Carga y retorna las traducciones personalizadas desde el archivo CSV
    """
    translations = {}
    
    # Obtener la ruta del archivo de traducciones
    app_path = frappe.get_app_path("tienda_mixta")
    translations_file = os.path.join(app_path, "translations", "es.csv")
    
    if os.path.exists(translations_file):
        try:
            with open(translations_file, 'r', encoding='utf-8') as file:
                # Leer el archivo CSV ignorando líneas de comentario
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Ignorar líneas vacías y comentarios
                    if not line or line.startswith('#'):
                        continue
                    
                    # Procesar líneas CSV
                    try:
                        # Usar csv.reader para manejar comillas y comas correctamente
                        row = list(csv.reader([line]))[0]
                        
                        if len(row) >= 2:
                            original = row[0].strip()
                            traduccion = row[1].strip()
                            
                            # Solo agregar si ambos campos tienen contenido
                            if original and traduccion:
                                translations[original] = traduccion
                                
                    except (csv.Error, IndexError) as e:
                        frappe.log_error(f"Error procesando línea {line_num} en traducciones: {str(e)}")
                        continue
                        
        except Exception as e:
            frappe.log_error(f"Error cargando traducciones personalizadas: {str(e)}")
    
    return translations

def load_custom_translations():
    """
    Función para cargar manualmente las traducciones personalizadas
    Útil para debugging o recarga manual
    """
    translations = get_translations()
    
    if translations:
        # Aplicar las traducciones al contexto actual
        for original, traduccion in translations.items():
            frappe._(original)  # Registrar la cadena para traducir
    
    return translations

def apply_custom_translations():
    """
    Aplica las traducciones personalizadas al sistema actual
    """
    translations = get_translations()
    
    # Obtener el diccionario de traducciones actual
    current_lang = frappe.local.lang or 'es'
    
    if current_lang == 'es' and translations:
        # Aplicar nuestras traducciones personalizadas
        if not hasattr(frappe.local, 'custom_translations'):
            frappe.local.custom_translations = {}
        
        frappe.local.custom_translations.update(translations)
        
        # Hook into the translation function
        original_translate = frappe._
        
        def custom_translate(text, lang=None):
            if lang == 'es' or (not lang and current_lang == 'es'):
                if hasattr(frappe.local, 'custom_translations') and text in frappe.local.custom_translations:
                    return frappe.local.custom_translations[text]
            return original_translate(text, lang)
        
        # Replace the original function
        frappe._ = custom_translate

@frappe.whitelist()
def reload_translations():
    """
    Función para recargar las traducciones personalizadas vía API
    """
    try:
        translations = load_custom_translations()
        apply_custom_translations()
        frappe.clear_cache()
        return {
            "success": True,
            "message": f"Traducciones recargadas exitosamente. {len(translations)} cadenas cargadas.",
            "translations_count": len(translations)
        }
    except Exception as e:
        frappe.log_error(f"Error recargando traducciones: {str(e)}")
        return {
            "success": False,
            "message": f"Error recargando traducciones: {str(e)}"
        }

def get_custom_translation(text, lang='es'):
    """
    Obtiene una traducción personalizada específica
    """
    translations = get_translations()
    if lang == 'es' and text in translations:
        return translations[text]
    return None

# Hook para inicializar las traducciones automáticamente
def on_session_creation(login_manager):
    """
    Hook que se ejecuta cuando se crea una sesión
    """
    if frappe.local.lang == 'es':
        apply_custom_translations()

def on_login(login_manager):
    """
    Hook que se ejecuta al hacer login
    """
    if frappe.local.lang == 'es':
        apply_custom_translations()