#!/usr/bin/env node

import { Command } from "commander";
import fetch from "node-fetch";
import admZip from "adm-zip";
import fs from "fs";
import path from "path";

const program = new Command();
const validFonts = ["sans", "mono", "all"];

const OUTPUT_DIRECTORY = "./geist-fonts";

const moveFontFiles = (srcDir, destDir) => {
  fs.readdir(srcDir, (err, files) => {
    if (err) throw err;

    files.forEach((file) => {
      if (path.extname(file) === ".woff2") {
        const srcPath = path.join(srcDir, file);
        const destPath = path.join(destDir, file);

        fs.rename(srcPath, destPath, (err) => {
          if (err) throw err;
        });
      }
    });
  });
};

const downloadFont = async (fontName, downloadUrl, isAll) => {
  console.log(
    `Downloading Geist ${fontName[0].toUpperCase() + fontName.slice(1)}`
  );
  const response = await fetch(downloadUrl);

  // Read the response as a buffer
  const bufferData = await response?.arrayBuffer();

  // Create a temporary file path for saving the downloaded zip
  const tempFilePath = `./temp/geist-${fontName}.zip`;

  if (!fs.existsSync("./temp")) {
    // If not, create it
    fs.mkdirSync("./temp", { recursive: true });
  }
  // Write the buffer data to disk as a zip file
  //   fs.writeFileSync(tempFilePath, Buffer.from(bufferData));

  // Extract files from the downloaded zip archive
  const unzipper = new admZip(tempFilePath);
  unzipper.extractAllTo(`./temp/geist-${fontName}`, true);

  const outputPath = `${OUTPUT_DIRECTORY}/${fontName}`;
  if (!fs.existsSync(outputPath)) {
    // If not, create it
    fs.mkdirSync(outputPath, { recursive: true });
  }

  if (fontName === "all" || fontName === "mono") {
    moveFontFiles(`./temp/geist-mono/Geist Mono`, outputPath);
    writeEntryFiles("mono", isAll);
  }
  if (fontName === "all" || fontName === "sans") {
    moveFontFiles(`./temp/geist-sans/Geist`, outputPath);
    writeEntryFiles("sans", isAll);
  }
};

const writeEntryFiles = (fontName, isAll) => {
  const fileName = "fonts.js";
  const outputPath = `${OUTPUT_DIRECTORY}/${fileName}`;
  if (!fs.existsSync(OUTPUT_DIRECTORY)) {
    // If not, create it
    fs.mkdirSync(OUTPUT_DIRECTORY, { recursive: true });
  }

  // Check if the file exists
  if (!fs.existsSync(outputPath)) {
    // Create the file
    fs.writeFileSync(outputPath, "", { flag: "wx" });
  }

  const importLine = `import localFont from 'next/font/local'`;

  const fontWeights = [
    { weight: "100", name: "Thin" },
    { weight: "200", name: "UltraLight" },
    { weight: "300", name: "Light" },
    { weight: "400", name: "Regular" },
    { weight: "500", name: "Medium" },
    { weight: "600", name: "SemiBold" },
    { weight: "700", name: "Bold" },
    { weight: "800", name: "Black" },
    { weight: "900", name: "UltraBlack" },
  ];

  if (fontName === "mono") {
    const code = `${importLine}\n\nexport const geistMono = localFont({
  src: [
${fontWeights
  .map((weight) => {
    return `    {
      path: './mono/GeistMonoBeta-${weight.name}.woff2',
      weight: '${weight.weight}',
      style: 'normal'
    }`;
  })
  .join(",\n")}
  ]
})`;

    fs.appendFile(outputPath, code, (err) => {
      if (err) throw err;
    });
  }

  if (fontName === "sans") {
    const code = `${
      !isAll ? `${importLine}\n\n` : "\n\n"
    }export const geistSans = localFont({
  src: [
${fontWeights
  .map((weight) => {
    return `    {
      path: './mono/GeistBeta-${weight.name}.woff2',
      weight: '${weight.weight}',
      style: 'normal'
    }`;
  })
  .join(",\n")}
  ]
})`;

    fs.appendFile(outputPath, code, (err) => {
      if (err) throw err;
    });
  }
};

const downloadFonts = async (font) => {
  const owner = "rsms";
  const repoName = "inter";
  const latestReleaseURL = `https://api.github.com/repos/${owner}/${repoName}/releases/latest`;

  const latestReleaseResponse = await fetch(latestReleaseURL);
  const { assets } = await latestReleaseResponse.json();
  const [monoRelease, sansRelease] = assets;

  switch (font) {
    case "sans":
      await downloadFont("sans", sansRelease.browser_download_url);
      break;
    case "mono":
      await downloadFont("mono", monoRelease.browser_download_url, false);
      break;
    case "all":
      await downloadFont("mono", monoRelease.browser_download_url, true);
      await downloadFont("sans", sansRelease.browser_download_url);
      break;
  }
};

function deleteDirectory(dirPath) {
  if (fs.existsSync(dirPath)) {
    fs.readdirSync(dirPath).forEach((file, index) => {
      const curPath = path.join(dirPath, file);
      if (fs.lstatSync(curPath).isDirectory()) {
        // recurse
        deleteDirectory(curPath);
      } else {
        // delete file
        fs.unlinkSync(curPath);
      }
    });
    fs.rmdirSync(dirPath);
  } else {
    console.log(`Directory not found: ${dirPath}`);
  }
}

program
  .command("download <font>")
  .description(
    `Downloads one or all the fonts: options are ${validFonts.join(", ")}`
  )
  .action(async (font) => {
    if (!validFonts.includes(font)) {
      console.log(
        `You tried downloading "${font}". Please use one of: ${validFonts.join(
          ", "
        )}`
      );
      process.exit(1);
    }

    await downloadFonts(font);

    // TODO: handle cleanup
    deleteDirectory("./temp");
  });

program.parse(process.argv);
