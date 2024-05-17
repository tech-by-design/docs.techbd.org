import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://tech-by-design.github.io',
	base: 'docs.techbd.org',
	integrations: [
		starlight({
			title: 'TechBD Docs',
			head: [{
				tag: "script",
				attrs: {
					type: "module",
					defer: true
				},
				content: `
					import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs'; 
					mermaid.initialize({ startOnLoad: true }); 
					await mermaid.run({
						querySelector: 'pre[data-language="mermaid"]',
				  	});`
			}],
			social: {
				github: 'https://github.com/tech-by-design/docs.techbd.org',
			},
			sidebar: [
				{
					label: 'Introduction to TechBD',
					link: 'techbd-intro',
				},
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
