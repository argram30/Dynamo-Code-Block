start = DSCore.List.GetItemAtIndex(a<2>,0);
end = DSCore.List.GetItemAtIndex(a<2>,1);
v1 = Autodesk.Vector.ByTwoPoints(start,end);
width = v1.X;
height = v1.Y;