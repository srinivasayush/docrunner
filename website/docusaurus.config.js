/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
    title: 'Docrunner',
    tagline:
        'Run your documentation reliably to allow readers to have access to working code',
    url: 'https://your-docusaurus-test-site.com',
    baseUrl: '/',
    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'warn',
    favicon: 'img/favicon.ico',
    organizationName: 'DudeBro249', // Usually your GitHub org/user name.
    projectName: 'docrunner', // Usually your repo name.
    themeConfig: {
        navbar: {
            title: 'Docrunner',
            logo: {
                alt: 'My Site Logo',
                src: 'img/logo.svg',
            },
            items: [
                {
                    type: 'doc',
                    docId: 'getting-started',
                    position: 'left',
                    label: 'Docs',
                },
                {
                    href: 'https://github.com/DudeBro249/docrunner',
                    label: 'GitHub',
                    position: 'right',
                },
            ],
        },
        footer: {
            style: 'dark',
            links: [
                {
                    title: 'Docs',
                    items: [
                        {
                            label: 'Tutorial',
                            to: '/docs/getting-started',
                        },
                    ],
                },
                {
                    title: 'Community',
                },
                {
                    title: 'More',
                    items: [
                        {
                            label: 'GitHub',
                            href: 'https://github.com/DudeBro249/docrunner',
                        },
                    ],
                },
            ],
            copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
        },
    },
    presets: [
        [
            '@docusaurus/preset-classic',
            {
                docs: {
                    sidebarPath: require.resolve('./sidebars.js'),
                    // Please change this to your repo.
                    editUrl:
                        'https://github.com/DudeBro249/docrunner/tree/main/website',
                },
                theme: {
                    customCss: require.resolve('./src/css/custom.css'),
                },
            },
        ],
    ],
}
