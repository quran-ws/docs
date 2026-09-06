import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://quran-ws.github.io',
  base: '/guidelines',
  // Neither language is the root: /ar/ and /en/ mirror each other, as the
  // content directories do. The bare base redirects to the default locale.
  redirects: {
    '/': '/guidelines/ar/',
  },
  integrations: [
    starlight({
      title: 'Quran.ws Guidelines',
      description: 'Internal guidelines and open standards for the Quran.ws infrastructure.',
      defaultLocale: 'ar',
      locales: {
        // Arabic is the authoring source for text-adab and terminology.
        ar: { label: 'العربية', lang: 'ar', dir: 'rtl' },
        en: { label: 'English', lang: 'en' },
      },
      social: {
        github: 'https://github.com/quran-ws/guidelines',
      },
      sidebar: [
        { label: 'المدخل', translations: { en: 'Introduction' }, autogenerate: { directory: '01-intro' } },
        { label: 'النص القرآني', translations: { en: 'Quranic text' }, autogenerate: { directory: '02-quranic-text' } },
        { label: 'المصطلحات', translations: { en: 'Terminology' }, autogenerate: { directory: '03-terminology' } },
        { label: 'الإصدارات', translations: { en: 'Versioning' }, autogenerate: { directory: '04-versioning' } },
        { label: 'المصدر المفتوح', translations: { en: 'Open source' }, autogenerate: { directory: '05-open-source' } },
        { label: 'الهندسة', translations: { en: 'Engineering' }, autogenerate: { directory: '06-engineering' } },
      ],
      head: [
        { tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
        { tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true } },
        {
          tag: 'link',
          attrs: {
            rel: 'stylesheet',
            // Rubik for everything it covers; Noto Naskh Arabic only catches the
            // Quranic marks Rubik has no glyphs for. See custom.css.
            href: 'https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&family=Noto+Naskh+Arabic:wght@400..700&display=swap',
          },
        },
      ],
      customCss: ['./src/styles/custom.css'],
    }),
  ],
});
