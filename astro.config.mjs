import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://tech-by-design.github.io',
	base: 'docs.techbd.org',
	integrations: [
		starlight({
			title: 'TechBD Docs',
			social: {
				github: 'https://github.com/tech-by-design/docs.techbd.org',
			},
			sidebar: [
				{
					label: '1115 Waiver',
					items: [
						{ 
							label: "FHIR Services", 
							autogenerate: { directory: '1115-hub/fhir-services' } 
						}, { 
							label: "SFTP Services", 
							autogenerate: { directory: '1115-hub/sftp-services' } 
						}]
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
			],
		}),
	],
});
