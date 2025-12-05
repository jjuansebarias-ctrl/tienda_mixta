"""
Script para aplicar traducciones personalizadas de Tienda Mixta La 40
Ejecuta este comando para aplicar las traducciones: bench execute tienda_mixta.apply_translations.apply_all_translations
"""

import frappe
import os

def apply_all_translations():
    """
    Aplica todas las traducciones personalizadas al sistema
    """
    try:
        # Importar nuestro módulo de traducciones
        from tienda_mixta.translations import get_translations, apply_custom_translations
        
        # Cargar traducciones personalizadas
        custom_translations = get_translations()
        
        if not custom_translations:
            print("❌ No se encontraron traducciones personalizadas")
            return
            
        print(f"📚 Cargando {len(custom_translations)} traducciones personalizadas...")
        
        # Aplicar traducciones
        apply_custom_translations()
        
        # Forzar recarga de traducciones en el sistema
        frappe.cache().delete_keys("lang_data")
        frappe.cache().delete_keys("bootinfo")
        
        print("✅ Traducciones aplicadas exitosamente")
        print("\n📋 Resumen de traducciones aplicadas:")
        
        # Mostrar algunas traducciones importantes
        important_translations = [
            "Login", "Password", "Email", "Remember me", "Forgot Password",
            "UOM", "Item Code", "Customer", "Supplier"
        ]
        
        for key in important_translations:
            if key in custom_translations:
                print(f"   • {key} → {custom_translations[key]}")
        
        print(f"\n💡 Total: {len(custom_translations)} traducciones personalizadas aplicadas")
        print("🔄 Reinicia el servidor con 'bench restart' para aplicar completamente los cambios")
        
        return True
        
    except Exception as e:
        print(f"❌ Error aplicando traducciones: {str(e)}")
        frappe.log_error(f"Error en apply_all_translations: {str(e)}")
        return False

def check_missing_translations():
    """
    Verifica qué traducciones faltan en el sistema
    """
    try:
        # Lista de cadenas comunes que deberían estar traducidas
        common_strings = [
            "Login", "Password", "Email", "Email Address", "Username",
            "Remember me", "Forgot Password", "Reset Password", "Sign Up",
            "Create Account", "Back to Login", "UOM", "Item Code",
            "Customer", "Supplier", "Save", "Cancel", "Submit"
        ]
        
        print("🔍 Verificando traducciones en el sistema...")
        
        missing = []
        existing = []
        
        for string in common_strings:
            # Verificar si existe traducción
            translated = frappe._(string, lang='es')
            if translated == string:  # No se tradujo
                missing.append(string)
            else:
                existing.append((string, translated))
        
        if missing:
            print(f"\n❌ {len(missing)} traducciones faltantes:")
            for item in missing:
                print(f"   • {item}")
        
        if existing:
            print(f"\n✅ {len(existing)} traducciones existentes:")
            for original, translated in existing:
                print(f"   • {original} → {translated}")
                
        return {"missing": missing, "existing": existing}
        
    except Exception as e:
        print(f"❌ Error verificando traducciones: {str(e)}")
        return None

@frappe.whitelist()
def reload_and_check():
    """
    Función para recargar y verificar traducciones via web
    """
    try:
        result = apply_all_translations()
        check = check_missing_translations()
        
        return {
            "success": result,
            "message": "Traducciones procesadas",
            "missing_count": len(check["missing"]) if check else 0,
            "existing_count": len(check["existing"]) if check else 0
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error: {str(e)}"
        }