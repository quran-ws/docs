import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import { glob } from 'astro/loaders';
import { z } from 'astro:content';

// Content lives in ../content so it stays readable on GitHub without a build.
export const collections = {
  docs: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: '../content' }),
    schema: docsSchema({
      extend: z.object({
        // Only `adopted` pages bind our projects.
        status: z.enum(['draft', 'proposed', 'adopted']).default('draft'),
      }),
    }),
  }),
};
