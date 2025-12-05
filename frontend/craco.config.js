module.exports = {
  style: {
    postcss: {
      mode: "file",
      loaderOptions: {
        postcssOptions: {
          plugins: [
            require("@tailwindcss/postcss"),
            require("autoprefixer"),
          ],
        },
      },
    },
  },
};