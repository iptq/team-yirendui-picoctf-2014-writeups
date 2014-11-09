# Internet Inspection - 30

## Problem

On his computer, your father left open a browser with the [Thyrin Lab Website](Thyrin Lab.html). Can you find the hidden access code?

## Hint

It may be helpful to learn how to 'Inspect Elements' in your browser.

## Writeup

Like the hint says, using Inspect Elements in Chrome on the webpage reveals a `<style>...</style>` line and a `<div id="checkers" style="position: absolute; top: 184.65625px; left: 490px; z-index: 100; width: 938px; height: 137px; overflow: hidden; background-image: url(https://picoctf.com/problem-static/web/internet-inspection/checkers.png);"></div>` line.

The first line contains code responsible for blurring the table and the second contains the checkers. Remove both of these lines from the code by selecting them and pressing Delete. The table should contain the resulting flag.

## Flag

flag_e8f910e5f83893d2f7bc1229ca444cdc03be56d2