import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  root: 'src',  // Tell Vite your entry point is in the src folder
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    outDir: '../static', // Build files go into the Flask 'static' folder
    emptyOutDir: true     // Clears the old build files
  }
})
