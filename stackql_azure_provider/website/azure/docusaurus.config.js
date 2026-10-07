import {themes as prismThemes} from 'prism-react-renderer';
import { createConfig } from './.shared-config/index.js';
import { providerName, providerTitle } from './provider.js';

const config = createConfig({
  providerName,
  providerTitle,
  prismThemes,
  overrides: {
    // Docusaurus Faster (rspack + swc, via @docusaurus/faster), consistent
    // with the other provider microsites.
    future: {
      v4: true,
      faster: true,
    },
  },
});

// No "Last updated on ..." stamps here: Docusaurus derives them from
// git log --name-status over the whole repository, and this repo is a fork
// of the azure-sdk-for-python monorepo whose history overflows the buffer
// (MaxBufferError). The shared default (off) stays in force.

// All four Azure microsites are mastered in the stackql-provider-azure
// monorepo, so the shared config's providerRepo derivation
// (stackql-provider-<name-sans-underscores>) and its edit link do not apply.
config.projectName = 'stackql-provider-azure';
config.presets[0][1].docs.editUrl =
  'https://github.com/stackql-registry/stackql-provider-azure/edit/stackql-provider/stackql_azure_provider/website/azure/';

// Use the locally vendored registry-branded logos (STACKQL>> | REGISTRY)
// instead of the shared config's hotlinked main-site wordmark -
// self-contained assets, no cross-origin fetch. global.css swaps in the
// -mobile variants below 996px.
const registryLogo = {
  alt: 'StackQL',
  href: '/',
  src: 'img/stackql-registry-logo.svg',
  srcDark: 'img/stackql-registry-logo-white.svg',
};
config.themeConfig.navbar.logo = { ...registryLogo };
config.themeConfig.footer.logo = { ...registryLogo };

// URL form. Keep the Docusaurus default (pages emitted as <route>/index.html)
// regardless of the shared config's trailingSlash setting, so GitHub Pages
// serves both /services/x/y and /services/x/y/. A trailingSlash: false site
// emits <route>.html instead, which returns 404 for the trailing-slash URL.
delete config.trailingSlash;

export default config;
