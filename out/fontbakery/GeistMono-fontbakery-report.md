## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[11] GeistMono[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 833 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- less_exclam_hyphen_hyphen_hyphen.liga

- numbersign_underscore.liga

- numbersign_underscore_parenleft.liga

- period_period_equal.liga

- slash_equal_equal.liga

- uni0306.cy
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
asciitilde_asciitilde_greater.liga, hyphen_hyphen_hyphen_greater.liga, less_exclam_hyphen_hyphen_hyphen.liga, numbersign_numbersign_numbersign.liga and numbersign_underscore_parenleft.liga</p>
 [code: legacy-long-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/GeistMono/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02B9 MODIFIER LETTER PRIME: not included in any glyphset definition</li>
<li>U+02C7 CARON: try adding one of: tifinagh, canadian-aboriginal, yi</li>
<li>U+02C8 MODIFIER LETTER VERTICAL LINE: not included in any glyphset definition</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, syriac, canadian-aboriginal, tai-le, tifinagh, math</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+039B GREEK CAPITAL LETTER LAMDA: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03BB GREEK SMALL LETTER LAMDA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2076 SUPERSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2079 SUPERSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2080 SUBSCRIPT ZERO: not included in any glyphset definition</li>
<li>U+2081 SUBSCRIPT ONE: not included in any glyphset definition</li>
<li>U+2082 SUBSCRIPT TWO: not included in any glyphset definition</li>
<li>U+2083 SUBSCRIPT THREE: not included in any glyphset definition</li>
<li>U+2084 SUBSCRIPT FOUR: not included in any glyphset definition</li>
<li>U+2085 SUBSCRIPT FIVE: not included in any glyphset definition</li>
<li>U+2086 SUBSCRIPT SIX: not included in any glyphset definition</li>
<li>U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition</li>
<li>U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition</li>
<li>U+2089 SUBSCRIPT NINE: not included in any glyphset definition</li>
<li>U+2107 EULER CONSTANT: not included in any glyphset definition</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: not included in any glyphset definition</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: not included in any glyphset definition</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: not included in any glyphset definition</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: not included in any glyphset definition</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: not included in any glyphset definition</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+219D RIGHTWARDS WAVE ARROW: try adding math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math</li>
<li>U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math</li>
<li>U+21B4 RIGHTWARDS ARROW WITH CORNER DOWNWARDS: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21E4 LEFTWARDS ARROW TO BAR: try adding math</li>
<li>U+21E5 RIGHTWARDS ARROW TO BAR: try adding math</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2326 ERASE TO THE RIGHT: try adding symbols</li>
<li>U+2327 X IN A RECTANGLE BOX: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+23CE RETURN SYMBOL: try adding symbols</li>
<li>U+240B SYMBOL FOR VERTICAL TABULATION: try adding symbols</li>
<li>U+240C SYMBOL FOR FORM FEED: try adding symbols</li>
<li>U+2423 OPEN BOX: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: symbols, yi, mongolian</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: symbols, yi, mongolian</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: symbols, yi, mongolian</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: symbols, yi, mongolian</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: symbols, yi, mongolian</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: symbols, yi, mongolian</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: symbols, yi, mongolian</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: symbols, yi, mongolian</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: symbols, yi, mongolian</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+2500 BOX DRAWINGS LIGHT HORIZONTAL: not included in any glyphset definition</li>
<li>U+2502 BOX DRAWINGS LIGHT VERTICAL: not included in any glyphset definition</li>
<li>U+250C BOX DRAWINGS LIGHT DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2514 BOX DRAWINGS LIGHT UP AND RIGHT: not included in any glyphset definition</li>
<li>U+251C BOX DRAWINGS LIGHT VERTICAL AND RIGHT: not included in any glyphset definition</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: coptic, devanagari, balinese, sharada, dogra, manichaean, limbu, khojki, masaram-gondi, adlam, meetei-mayek, mahajani, kannada, armenian, khmer, marchen, myanmar, nko, grantha, gunjala-gondi, lepcha, pahawh-hmong, psalter-pahlavi, tagbanwa, tagalog, thaana, tai-tham, zanabazar-square, kaithi, buginese, symbols, thai, saurashtra, takri, yi, duployan, ahom, tifinagh, batak, brahmi, oriya, tirhuta, sundanese, sogdian, warang-citi, osage, wancho, canadian-aboriginal, syloti-nagri, tai-le, tai-viet, chakma, caucasian-albanian, khudawadi, newa, old-permic, new-tai-lue, elbasan, kharoshthi, tamil, bhaiksuki, bassa-vah, math, rejang, sinhala, hebrew, hanunoo, lao, javanese, phags-pa, cham, hanifi-rohingya, buhid, syriac, mende-kikakui, kayah-li, modi, tibetan, bengali, music, gurmukhi, mongolian, telugu, malayalam, miao, siddham, soyombo, mandaic, gujarati</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+3003 DITTO MARK: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified</li>
<li>U+3008 LEFT ANGLE BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, tai-le, yi, chinese-traditional, chinese-simplified</li>
<li>U+3009 RIGHT ANGLE BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, tai-le, yi, chinese-traditional, chinese-simplified</li>
<li>U+300A LEFT DOUBLE ANGLE BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, lisu, tai-le, yi, chinese-traditional, chinese-simplified, mongolian</li>
<li>U+300B RIGHT DOUBLE ANGLE BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, lisu, tai-le, yi, chinese-traditional, chinese-simplified, mongolian</li>
<li>U+300C LEFT CORNER BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified, mongolian</li>
<li>U+300D RIGHT CORNER BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified, mongolian</li>
<li>U+300E LEFT WHITE CORNER BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified, mongolian</li>
<li>U+300F RIGHT WHITE CORNER BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified, mongolian</li>
<li>U+3010 LEFT BLACK LENTICULAR BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified</li>
<li>U+3011 RIGHT BLACK LENTICULAR BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified</li>
<li>U+3014 LEFT TORTOISE SHELL BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified</li>
<li>U+3015 RIGHT TORTOISE SHELL BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified</li>
<li>U+3016 LEFT WHITE LENTICULAR BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified</li>
<li>U+3017 RIGHT WHITE LENTICULAR BRACKET: try adding one of: japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, chinese-simplified</li>
<li>U+301C WAVE DASH: try adding japanese</li>
<li>U+F8FF : not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: į̆ į̇ į̈ į̊ į̋ į̒ į̦̀ į̦́ į̦̂ į̦̃ į̦̄ į̦̆ į̦̇ į̦̈ į̦̊ į̦̋ į̦̌ į̦̒ į̧̀ į̧́</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Navajo (Latn, 166,319 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Koonzime (Latn, 40,000 speakers), Dii (Latn, 71,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Makaa (Latn, 221,000 speakers), Cicipu (Latn, 44,000 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Igbo (Latn, 27,823,640 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Mfumte (Latn, 79,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Mundani (Latn, 34,000 speakers), Nzakara (Latn, 50,000 speakers), Ebira (Latn, 2,200,000 speakers), Vute (Latn, 21,000 speakers), Southern Kisi (Latn, 360,000 speakers), Bafut (Latn, 158,146 speakers), Mango (Latn, 77,000 speakers), Ekpeye (Latn, 226,000 speakers), South Central Banda (Latn, 244,000 speakers), Gulay (Latn, 250,478 speakers), Aghem (Latn, 38,843 speakers), Sar (Latn, 500,000 speakers), Lugbara (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Basaa (Latn, 332,940 speakers), Ma’di (Latn, 584,000 speakers), Yala (Latn, 200,000 speakers), Fur (Latn, 1,230,163 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* blackCircled has a counter-clockwise outer contour

* uni24FF (U+24FF) has a counter-clockwise outer contour

* uni2776 (U+2776) has a counter-clockwise outer contour

* uni2777 (U+2777) has a counter-clockwise outer contour

* uni2778 (U+2778) has a counter-clockwise outer contour

* uni2779 (U+2779) has a counter-clockwise outer contour

* uni277A (U+277A) has a counter-clockwise outer contour

* uni277B (U+277B) has a counter-clockwise outer contour

* uni277C (U+277C) has a counter-clockwise outer contour

* uni277D (U+277D) has a counter-clockwise outer contour

* uni277E (U+277E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID value 'VRCL' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 11 | 95 | 8 | 137 | 0 | 
| 0% | 0% | 0% | 4% | 38% | 3% | 55% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
