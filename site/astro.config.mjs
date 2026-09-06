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
      customCss: ['./src/styles/custom.css'],
    }),
  ],
});
