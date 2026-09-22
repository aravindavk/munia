import std.stdio;
import std.json;
import std.file : readText;
import std.algorithm.iteration : map;
import std.array : array;

import chitra;

enum DotType
{
    circle,
    square
}

void drawGlyph(Chitra ctx, string name, int[] cells, DotType ty = DotType.init)
{
    with (ctx)
    {
        newDrawing;
        noStroke;
        grid(5, 7, gap: 10);
        gridSize(0, 100, 500, 710);
        fill(0);
        ovalMode(CORNER);

        foreach(n; cells)
        {
            if (ty == DotType.circle)
                oval(gridCell(n));
            else
                rect(gridCell(n));
                
        }

        if (ty == DotType.circle)
            saveAs("glyphs/" ~ name ~ ".svg");
        else
            saveAs("glyphs/" ~ name ~ ".ss01.svg");
    }
}

int main(string[] args)
{
    auto ctx = new Chitra(1000);

    auto glyphsData = parseJSON(readText("glyphs.json"));
    
    with (ctx)
    {
        foreach(glyph; glyphsData.array)
        {
            drawGlyph(ctx, glyph["name"].str, glyph["data"].array.map!(x => x.get!int).array, ty: DotType.circle);
            drawGlyph(ctx, glyph["name"].str, glyph["data"].array.map!(x => x.get!int).array, ty: DotType.square);
        }
    }

    return 0;
}
