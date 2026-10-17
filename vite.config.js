import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

const adapter = process.env.RENDER
  ? (await import('@sveltejs/adapter-node')).default
  : (await import('@sveltejs/adapter-static')).default;

export default defineConfig({
  plugins: [
    sveltekit({
      compilerOptions: {
        runes: ({ filename }) => filename.split(/[/\\]/).includes('node_modules') ? undefined : true
      },
      adapter: process.env.RENDER ? adapter() : adapter({ fallback: '404.html' }),
      paths: { base: process.env.GITHUB_ACTIONS ? '/front-parcial-1-corte' : '' }
    })
  ]
});
