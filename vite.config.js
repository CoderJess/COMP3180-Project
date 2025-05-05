import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path';

export default defineConfig({
  plugins: [vue()],
  root: './',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  build:{
    outDir: 'app/static',
    emptyOutDir: true,
  }
});
