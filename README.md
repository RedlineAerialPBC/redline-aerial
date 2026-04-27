# Redline Aerial Website

Marketing site for Redline Aerial, built with React + Vite + Tailwind CSS.

## Local development

```bash
npm install
npm run dev
```

## Build and quality checks

```bash
npm run lint
npm run build
```

## What was improved

- Replaced a remote hero image URL with a local bundled asset to improve reliability and reduce third-party dependency risk.
- Added business-focused SEO metadata in `index.html` (title, description, Open Graph, and Twitter tags).
- Improved contact accessibility by making the email in the contact card an actual clickable `mailto:` link.

## Recommended next improvements

- Add a dedicated lead form with validation and spam protection (e.g., Netlify Forms, Formspree, or a serverless endpoint).
- Add analytics + conversion tracking (GA4 and ad platform pixels) to measure quote requests.
- Add a real project gallery/testimonials section to increase trust and conversion rate.
- Add a custom domain canonical URL update in `index.html` if the production domain changes.
