import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'TechBD Docs',
			social: {
				github: 'https://github.com/withastro/starlight',
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
