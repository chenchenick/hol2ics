import { Config } from "./src/config";

export const defaultConfig: Config = {
  url: "https://developer.salesforce.com/sitemap-1.xml",
  match: "https://developer.salesforce.com/docs/**",
  maxPagesToCrawl: 20000,
  outputFileName: "sfdocs.json",
  maxTokens: 1024,
};
