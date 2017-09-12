#### CSS Syntax
----------------------------------------------------
selector       declaration            declaration
h1         { color  :  blue;   font-size   :  12px;}
             Property  Value    Property     Value
-----------------------------------------------------
The selector points to the HTML element you want to style.
The declaration block contains one or more declarations separated by semicolons.
Each declaration includes a CSS property name and a value, separated by a colon.
A CSS declaration always ends with a semicolon, and declaration blocks are surrounds by curly braces

1. selector
  - HTML中的元素
  - ID
  - class : class = "center"

2. comment: /*    */

#### How to use CSS
  - External style sheet
  - Internal style sheet
  - Inline style

1. External style sheet
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

2. Internal style sheet
<head>
<style>
body{
    background-color: Linen;
}
h1{
    color: maroon;
    margin-left: 40px;
}
</style>
</head>

3. Inline style
<h1 style="color:blue;margin-left:30px;">This is a heading</h1>


#### CSS Property
1. CSS Colors
   - a valid color name - like "red"
   - an RGB value -like "rgb(255,0,0)"
   - a HEX value -like "#ff0000"

2. CSS Backgrounds
   - background-color
   - background-image
   - background-repeat
   - background-attachment
   - background-position