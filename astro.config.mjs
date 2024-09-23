import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://tech-by-design.github.io',
	base: 'docs.techbd.org',
	integrations: [
		starlight({
			title: 'Documentation',
			logo: {
				light: '/src/assets/tech-by-design_doc_full-color_small.png',
				dark: '/src/assets/tech-by-design_doc_full-color_small.png',
				replacesTitle: true,
			},
			customCss: [
				// Relative path to your custom CSS file
				'./src/styles/custom.css',
			  ],
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
			editLink: {
				baseUrl: 'https://github.com/tech-by-design/docs.techbd.org/edit/main/',
			},
			social: {
				github: 'https://github.com/tech-by-design/docs.techbd.org',
			},
			sidebar: [
				{
					label: 'Introduction to Tech by Design',
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
					label: 'Developer Experience',
					autogenerate: { directory: 'dx' },
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
				{
					label: 'Collaboration Hub',
					items: [
						{
							label: "login",
							autogenerate: { directory: 'collaborationhub/login' }
						},{
							label: "Overview",
							autogenerate: { directory: 'collaborationhub/overview' }
						},						
						{
							label: "Dashboard",
							autogenerate: { directory: 'collaborationhub/dashboard' }
						},
						{
							label: "Content",
							autogenerate: { directory: 'collaborationhub/content' }
						}]
				},
			],
		}),
	],
});