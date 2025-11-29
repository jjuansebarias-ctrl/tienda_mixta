import frappe

def get_website_context():
    """
    Función para inyectar contexto personalizado en todas las páginas web
    incluyendo login, favicon y otros elementos de branding
    """
    return {
        "brand_logo": "/assets/tienda_mixta/images/licores-la-40-logo.png",
        "favicon": "/assets/tienda_mixta/images/licores-la-40-logo.png",
        "logo": "/assets/tienda_mixta/images/licores-la-40-logo.png",
        "app_logo_url": "/assets/tienda_mixta/images/licores-la-40-logo.png"
    }