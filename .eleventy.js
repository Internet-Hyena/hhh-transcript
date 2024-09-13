const { EleventyRenderPlugin } = require("@11ty/eleventy");

module.exports = function(eleventyConfig) {
  eleventyConfig.addPlugin(EleventyRenderPlugin);

  eleventyConfig.addPassthroughCopy("src/images/");
  // Return your Object options:
  return {
    dir: {
      input: "src",
      output: "_site"
    }
  }
};