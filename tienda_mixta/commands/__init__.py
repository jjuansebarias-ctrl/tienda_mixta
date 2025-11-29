"""
Comando para corregir traducciones problemáticas en ERPNext
"""

import click
import frappe
import os
import csv
import re
from frappe.commands import pass_context


def init(context):
    pass


@click.command('fix-translations')
@click.option('--app', default='erpnext', help='App to fix translations for')
@pass_context
def fix_translations(context, app):
    """
    Comando para corregir traducciones problemáticas en ERPNext
    
    Uso:
    bench --site <sitio> fix-translations
    bench --site <sitio> fix-translations --app erpnext
    """
    
    click.echo("🔧 Iniciando corrección de traducciones...")
    
    # Mapeo de correcciones específicas
    corrections = {
        # Correcciones de UOM -> UdM
        ",UOM,": ",UdM,",
        "Include UOM,Incluir UOM,": "Include UOM,Incluir UdM,",
        "Lab Test UOM,UOM de Prueba de Laboratorio,": "Lab Test UOM,UdM de Prueba de Laboratorio,",
        "Stock UOM,Unidad de media utilizada en el almacen,": "Stock UOM,UdM de Inventario,",
        
        # Correcciones de mensajes largos con UOM
        "ya ha realizado alguna transacción (s) con otra UOM": "ya ha realizado alguna transacción con otra UdM",
        "crear un nuevo elemento a utilizar un UOM predeterminado diferente": "crear un nuevo elemento a utilizar una UdM predeterminada diferente",
        "Unidad de Medida diferente para elementos dará lugar a Peso Neto (Total) incorrecto. Asegúrese de que el peso neto de cada artículo esté en la misma Unidad de Medida.": "Unidades de Medida diferentes para elementos resultarán en un Peso Neto (Total) incorrecto. Asegúrese de que el peso neto de cada artículo esté en la misma UdM.",
        "Factor de conversion de la Unidad de Medida requerido para la Unidad de Medida": "Factor de conversión de UdM requerido para la UdM",
        "El precio del artículo aparece varias veces según la Lista de precios, Proveedor / Cliente, Moneda, Artículo, UOM, Cantidad y fechas.": "El Precio del Artículo aparece múltiples veces basado en Lista de Precios, Proveedor/Cliente, Moneda, Artículo, UdM, Cantidad y Fechas.",
        "El factor de conversión de (UdM) es obligatorio": "El Factor de Conversión de UdM es obligatorio",
        "El factor de conversión de la (UdM) es requerido en la línea": "El factor de conversión de UdM es requerido en la fila",
        "Importar artículos y unidades de medida": "Importando Artículos y UdM",
        "Procesamiento de artículos y unidades de medida": "Procesando Artículos y UdM",
        
        # Correcciones gramaticales y de estilo
        "Cliente,": "Cliente,",
        "Proveedor,": "Proveedor,",
        "Empleado,": "Empleado,",
        "Empresa,": "Empresa,",
        "Cuenta,": "Cuenta,",
    }
    
    # Rutas de archivos a corregir
    translations_files = [
        f"apps/{app}/{app}/translations/es.csv",
    ]
    
    total_corrections = 0
    
    for file_path in translations_files:
        full_path = os.path.join(frappe.get_site_path(), "..", file_path)
        
        if not os.path.exists(full_path):
            click.echo(f"❌ Archivo no encontrado: {file_path}")
            continue
            
        click.echo(f"🔍 Procesando: {file_path}")
        
        try:
            # Leer el archivo
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Aplicar correcciones
            file_corrections = 0
            original_content = content
            
            for original, corrected in corrections.items():
                if original in content:
                    content = content.replace(original, corrected)
                    file_corrections += 1
            
            # Escribir el archivo corregido si hubo cambios
            if content != original_content:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                click.echo(f"✅ {file_corrections} correcciones aplicadas en {file_path}")
                total_corrections += file_corrections
            else:
                click.echo(f"ℹ️ No se necesitaron correcciones en {file_path}")
                
        except Exception as e:
            click.echo(f"❌ Error procesando {file_path}: {str(e)}")
    
    if total_corrections > 0:
        click.echo(f"\n🎉 Total de correcciones aplicadas: {total_corrections}")
        click.echo("💡 Ejecuta 'bench build' para aplicar los cambios")
        click.echo("💡 Ejecuta 'bench restart' para recargar el sistema")
    else:
        click.echo("\nℹ️ No se aplicaron correcciones. Las traducciones ya estaban correctas.")

commands = [
    fix_translations
]