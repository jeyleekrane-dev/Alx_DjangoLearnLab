# Security Measures

## Secure Settings
- DEBUG is set to False in production.
- SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF, CSRF_COOKIE_SECURE, and SESSION_COOKIE_SECURE are configured for enhanced security.

## CSRF Protection
- All form templates include `{% csrf_token %}` to protect against CSRF attacks.

## Safe Data Access
- Views use Django ORM for safe queries and validate user input using Django forms.

## Content Security Policy (CSP)
- CSP headers can be set using django-csp or manually in response objects to reduce XSS risks.

## Testing
- Manual tests are performed to check for CSRF and XSS vulnerabilities.
- Comments in code explain security settings and practices.
