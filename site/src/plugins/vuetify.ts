/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

const oceanTheme = {
  dark: true,
  colors: {
    background: "#233",
    surface: "#255",
    primary: "#244",
    secondary: "#244",
    error: "#ff5722",
  },
};

const inversityTheme = {
  dark: false,
  colors: {
    background: "#eee",
    surface: "#15202b",
    primary: "#3f51b5",
    secondary: "#00ccff",
    error: "#ffcc00",
  },
};

const nightTheme = {
  dark: true,
  colors: {
    background: "#111",
    surface: "#15202b",
    primary: "#3f51b5",
    secondary: "#00ccff",
    error: "#ffcc00",
  }
}

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    defaultTheme: 'inversityTheme',
    themes: {
      nightTheme,
      inversityTheme,
      oceanTheme
    },
  },
})
