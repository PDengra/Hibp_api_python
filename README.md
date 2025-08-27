# Hibp_api_python

🔐 Comprobando si una contraseña ha aparecido en filtraciones (HIBP API con Python)

En el ámbito de la ciberseguridad, es fundamental concienciar sobre el riesgo de reutilizar contraseñas o usar claves débiles.
He preparado un pequeño script en Python que permite verificar, de manera segura y anónima, si una contraseña aparece en bases de datos de brechas conocidas (usando la API pública de Have I Been Pwned y el método de k-anonymity).

👉 Lo interesante es que nunca se envía la contraseña completa a la API, solo un fragmento de su hash SHA-1, protegiendo así la privacidad del usuario.

✅ Lección clave: aunque tu contraseña no aparezca en filtraciones, no significa que sea segura. Siempre utiliza claves largas, únicas y, si es posible, un gestor de contraseñas.
