## FontSpector report

fontspector version: 1.6.0






## Check results




<details><summary>[3] </summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** GeistPixel[ELSH].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, coptic, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, malayalam, canadian-aboriginal, old-permic, syriac, duployan, tai-le, coptic, tifinagh, todhri, math
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
... and 46 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Check for presence of an ARTICLE.en_us.html file (googlefonts/description/has_article)</summary>
    <div>








- ℹ️ **INFO** This font doesn't have an ARTICLE.en_us.html file. [code: missing-article]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Check axis ordering on the STAT table. (googlefonts/STAT/axis_order)</summary>
    <div>








- ℹ️ **INFO** None of the fonts lack a STAT table.

	And these are the most common STAT axis orderings:
	ELSH: 1 [code: summary]
  
  

</div>
</details>


</div>
</details>


<details><summary>[20] GeistPixel[ELSH].ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check variable font instances (googlefonts/fvar_instances)</summary>
    <div>








- 🔥 **FAIL** fvar instances are incorrect:

- Delete additional instances

| Name     | current | expected |
|----------|---------|----------|
| Square   | ELSH=1  | N/A      |
| Circle   | ELSH=20 | N/A      |
| Grid     | ELSH=40 | N/A      |
| Triangle | ELSH=60 | N/A      |
| Line     | ELSH=80 | N/A      |
| Regular  | ELSH=0  | ELSH=0   |

 [code: bad-fvar-instances]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> 
    Validate STAT particle names and values match the fallback names in GFAxisRegistry.
     (googlefonts/STAT/axisregistry)</summary>
    <div>








- 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Regular' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
  
  


- 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Square' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
  
  


- 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Circle' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
  
  


- 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Grid' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
  
  


- 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Triangle' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
  
  


- 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Line' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check a font's STAT table contains compulsory Axis Values. (googlefonts/STAT/compulsory_axis_values)</summary>
    <div>








- 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

| Name    | Axis | Current Value | Expected Value | Current Flags | Expected Flags | Current Linked Value | Expected Linked Value |
|---------|------|---------------|----------------|---------------|----------------|----------------------|-----------------------|
| Regular | wght | N/A           | 400            | N/A           | 0              | N/A                  | 700                   |

 [code: bad-axis-values]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>








- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* C (U+0043): found 88, expected one of: [1, 2, 5]
* Cacute (U+0106): found 97, expected one of: [2, 3, 6]
* Ccaron (U+010C): found 102, expected one of: [2, 3, 6]
* Ccircumflex (U+0108): found 102, expected one of: [2, 3, 6]
* Cdotaccent (U+010A): found 94, expected one of: [2, 3, 6]
* uni018F (U+018F): found 118, expected one of: [1, 2]
* uni1E20 (U+1E20): found 123, expected one of: [2, 3, 4]
* I (U+0049): found 38, expected one of: [1, 2, 3]
* Iacute (U+00CD): found 47, expected one of: [2, 3, 4]
... and 240 others [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure files are not too large. (file_size)</summary>
    <div>








- ⚠️ **WARN** Font file is 3.66 MB; ideally it should be less than 1.05 MB [code: large-font]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. (mandatory_avar_table)</summary>
    <div>








- ⚠️ **WARN** The font does not include an avar table.  If the progression rates of axes is linear and no user-mapping is expected, this is fine, and this check can be ignored or excluded. [code: missing-avar]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>








- ⚠️ **WARN** The most common width is 532 among a set of 13  math glyphs.
The following math glyphs have a different width, though:
width=570: approxequal
width=494: minus, multiply, logicalnot
width=608: notequal, greaterequal, lessequal [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>








- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts have relatively consistent sidebearings. (suspicious_sidebearings)</summary>
    <div>








- ⚠️ **WARN** Glyph "uni2028" has suspiciously high variation (z-score 10.92) in right sidebearings at locations:
    ELSH=40.00 [code: large-rsb-variation]
  
  


- ⚠️ **WARN** Glyph "uni00A0" has suspiciously high variation (z-score 10.92) in right sidebearings at locations:
    ELSH=40.00 [code: large-rsb-variation]
  
  


- ⚠️ **WARN** Glyph "uni2029" has suspiciously high variation (z-score 10.92) in right sidebearings at locations:
    ELSH=40.00 [code: large-rsb-variation]
  
  


- ⚠️ **WARN** Glyph "space" has suspiciously high variation (z-score 10.92) in right sidebearings at locations:
    ELSH=40.00 [code: large-rsb-variation]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * de_Latn (German)           |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)          |
|   The following auxiliary characters are missing from the font: Ĕ |                              |
|   The following auxiliary characters are missing from the font: Ĭ |                              |
|   The following auxiliary characters are missing from the font: Ŀ |                              |
|   The following auxiliary characters are missing from the font: Ŏ |                              |
|   The following auxiliary characters are missing from the font: ĕ |                              |
|   The following auxiliary characters are missing from the font: ĭ |                              |
|   The following auxiliary characters are missing from the font: ŀ |                              |
|   The following auxiliary characters are missing from the font: ŏ |                              |
| Auxiliary orthography codepoints:                                 | * cs_Latn (Czech)            |
|   The following auxiliary characters are missing from the font: Ĕ | * cy_Latn (Welsh)            |
|   The following auxiliary characters are missing from the font: Ĭ | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: Ŏ | * es_Latn (Spanish)          |
|   The following auxiliary characters are missing from the font: ĕ | * hu_Latn (Hungarian)        |
|   The following auxiliary characters are missing from the font: ĭ | * pt_Latn (Portuguese)       |
|   The following auxiliary characters are missing from the font: ŏ | * sk_Latn (Slovak)           |
|                                                                   | * tr_Latn (Turkish)          |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. (dotted_circle)</summary>
    <div>








- ⚠️ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings:

* į̌
* į̀
* į̄
* į̂
* į̃
* į́The dot of soft dotted characters _should_ disappear in other cases, for example:

* į̊
* į̆
* į̇
* į̒
* į̈
* į̋ [code: soft-dotted]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have overlapping path segments:

* .notdef: Quad(QuadBez { p0: (133.0, 114.0), p1: (129.0, 114.0), p2: (124.0, 114.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (124.0, 114.0), p1: (119.0, 114.0), p2: (114.0, 114.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (152.0, 114.0), p1: (147.0, 114.0), p2: (142.5, 114.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (142.5, 114.0), p1: (138.0, 114.0), p2: (133.0, 114.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (133.0, 152.0), p1: (129.0, 152.0), p2: (124.0, 152.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (124.0, 152.0), p1: (119.0, 152.0), p2: (114.0, 152.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (152.0, 152.0), p1: (147.0, 152.0), p2: (142.5, 152.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (142.5, 152.0), p1: (138.0, 152.0), p2: (133.0, 152.0) }) has the same coordinates as a previous segment.
* .notdef: Quad(QuadBez { p0: (133.0, 190.0), p1: (129.0, 190.0), p2: (124.0, 190.0) }) has the same coordinates as a previous segment.
... and 225900 others [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'VRCL' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Checking OS/2 fsSelection value. (opentype/xavgcharwidth)</summary>
    <div>








- ℹ️ **INFO** OS/2 xAvgCharWidth is 551 but it should be 550 which corresponds to the average of the widths of all glyphs in the font. These are similar values, which may be a symptom of the slightly different calculation of the xAvgCharWidth value in font editors. There's further discussion on this at https://github.com/fonttools/fontbakery/issues/1622 [code: xAvgCharWidth-close]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Show hinting filesize impact. (hinting_impact)</summary>
    <div>








- ℹ️ **INFO** Hinting filesize impact:

 |               | GeistPixel[ELSH].ttf     |
 |:------------- | ---------------:|
 | Dehinted Size | 3657168 |
 | Hinted Size   | 3657192   |
 | Increase      | 24      |
 | Change        | 0.0 %  | [code: size-impact]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Font contains all required tables? (required_tables)</summary>
    <div>








- ℹ️ **INFO** This font contains the following optional tables:

    loca
    prep
    GPOS
    GSUB
    gasp [code: optional-tables]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>








- ℹ️ **INFO** These are the ppm ranges declared on the gasp table:

| PPM <= 65535 | - Use grid-fitting                                    |
|              | 	- Use grayscale rendering                            |
|              | 	- Use gridfitting with ClearType symmetric smoothing |
|              | 	- Use smoothing along multiple axes with ClearType®  |
|--------------|-------------------------------------------------------|
 [code: ranges]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ℹ️ **INFO** "Latn" [code: dlng-tag]
  
  


- ℹ️ **INFO** "Latn" [code: slng-tag]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Font has old ttfautohint applied? (googlefonts/old_ttfautohint)</summary>
    <div>








- ℹ️ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: Version 1.000 [code: version-not-detected]
  
  

</div>
</details>


</div>
</details>






### Summary

| 🔥 FAIL | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 8 | 15 | 9 | 110 | 57 | 
| 4% | 8% | 5% | 58% | 30% | 



