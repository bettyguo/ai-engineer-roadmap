/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        sans: [
          "Inter",
          "ui-sans-serif",
          "system-ui",
          "-apple-system",
          "Segoe UI",
          "Roboto",
          "sans-serif",
        ],
        serif: [
          "Source Serif Pro",
          "IBM Plex Serif",
          "Georgia",
          "serif",
        ],
        mono: [
          "JetBrains Mono",
          "ui-monospace",
          "SFMono-Regular",
          "Menlo",
          "monospace",
        ],
      },
      colors: {
        ink: {
          50: "#F8F7F4",
          100: "#EDEAE2",
          200: "#D9D2C3",
          900: "#0A0A0A",
          950: "#050505",
        },
        paper: {
          50: "#FAF8F2",
          100: "#F2EFE5",
          200: "#E6E0CC",
        },
      },
    },
  },
  plugins: [],
};
