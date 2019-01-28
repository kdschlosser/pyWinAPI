import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_FLATAPI_H = None


# ************************************************************************\
# Copyright (c) 1998-2001, Microsoft Corp. All Rights Reserved. Module Name:
# GdiplusFlat.h Abstract: Private GDI+ header file.
# \************************************************************************
if not defined(_FLATAPI_H):
    _FLATAPI_H = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        WINGDIPAPI = VOID
        GDIPCONST = VOID
        if defined(__cplusplus):
            pass
        # END IF

        GpStatus = VOID

        # ------------------------------------------------------------------
        # GraphicsPath APIs
        # ------------------------------------------------------------------
        gdiplus = ctypes.windll.GDIPLUS

        # GpStatus WINGDIPAPI
        # GdipCreatePath(GpFillMode brushMode, GpPath **path);
        GdipCreatePath = gdiplus.GdipCreatePath
        GdipCreatePath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreatePath2(GDIPCONST GpPointF*, GDIPCONST BYTE*, INT, GpFillMode,
        # GpPath **path);
        GdipCreatePath2 = gdiplus.GdipCreatePath2
        GdipCreatePath2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreatePath2I(GDIPCONST GpPoint*, GDIPCONST BYTE*, INT, GpFillMode,
        # GpPath **path);
        GdipCreatePath2I = gdiplus.GdipCreatePath2I
        GdipCreatePath2I.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathTypes(_In_ GpPath* path,
        # _Out_writes_bytes_(count) BYTE* types, INT count);
        GdipGetPathTypes = gdiplus.GdipGetPathTypes
        GdipGetPathTypes.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathFillMode(GpPath *path, GpFillMode *fillmode);
        GdipGetPathFillMode = gdiplus.GdipGetPathFillMode
        GdipGetPathFillMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathFillMode(GpPath *path, GpFillMode fillmode);
        GdipSetPathFillMode = gdiplus.GdipSetPathFillMode
        GdipSetPathFillMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathData(GpPath *path, GpPathData* pathData);
        GdipGetPathData = gdiplus.GdipGetPathData
        GdipGetPathData.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipStartPathFigure(GpPath *path);
        GdipStartPathFigure = gdiplus.GdipStartPathFigure
        GdipStartPathFigure.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipClosePathFigure(GpPath *path);
        GdipClosePathFigure = gdiplus.GdipClosePathFigure
        GdipClosePathFigure.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipClosePathFigures(GpPath *path);
        GdipClosePathFigures = gdiplus.GdipClosePathFigures
        GdipClosePathFigures.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathLine(GpPath *path, REAL x1, REAL y1, REAL x2, REAL y2);
        GdipAddPathLine = gdiplus.GdipAddPathLine
        GdipAddPathLine.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathLine2(GpPath *path, GDIPCONST GpPointF *points, INT count);
        GdipAddPathLine2 = gdiplus.GdipAddPathLine2
        GdipAddPathLine2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathArc(GpPath *path, REAL x, REAL y, REAL width, REAL height,
        # REAL startAngle, REAL sweepAngle);
        GdipAddPathArc = gdiplus.GdipAddPathArc
        GdipAddPathArc.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathBezier(GpPath *path, REAL x1, REAL y1, REAL x2, REAL y2,
        # REAL x3, REAL y3, REAL x4, REAL y4);
        GdipAddPathBezier = gdiplus.GdipAddPathBezier
        GdipAddPathBezier.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathBeziers(GpPath *path, GDIPCONST GpPointF *points, INT count);
        GdipAddPathBeziers = gdiplus.GdipAddPathBeziers
        GdipAddPathBeziers.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathCurve(GpPath *path, GDIPCONST GpPointF *points, INT count);
        GdipAddPathCurve = gdiplus.GdipAddPathCurve
        GdipAddPathCurve.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathCurve2(GpPath *path, GDIPCONST GpPointF *points, INT count,
        # REAL tension);
        GdipAddPathCurve2 = gdiplus.GdipAddPathCurve2
        GdipAddPathCurve2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathCurve3(GpPath *path, GDIPCONST GpPointF *points, INT count,
        # INT offset, INT numberOfSegments, REAL tension);
        GdipAddPathCurve3 = gdiplus.GdipAddPathCurve3
        GdipAddPathCurve3.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathClosedCurve(GpPath *path, GDIPCONST GpPointF *points, INT count);
        GdipAddPathClosedCurve = gdiplus.GdipAddPathClosedCurve
        GdipAddPathClosedCurve.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathClosedCurve2(GpPath *path, GDIPCONST GpPointF *points, INT count,
        # REAL tension);
        GdipAddPathClosedCurve2 = gdiplus.GdipAddPathClosedCurve2
        GdipAddPathClosedCurve2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathRectangle(GpPath *path, REAL x, REAL y, REAL width, REAL height);
        GdipAddPathRectangle = gdiplus.GdipAddPathRectangle
        GdipAddPathRectangle.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathRectangles(GpPath *path, GDIPCONST GpRectF *rects, INT count);
        GdipAddPathRectangles = gdiplus.GdipAddPathRectangles
        GdipAddPathRectangles.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathEllipse(GpPath *path, REAL x, REAL y, REAL width,
        # REAL height);
        GdipAddPathEllipse = gdiplus.GdipAddPathEllipse
        GdipAddPathEllipse.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathPie(GpPath *path, REAL x, REAL y, REAL width, REAL height,
        # REAL startAngle, REAL sweepAngle);
        GdipAddPathPie = gdiplus.GdipAddPathPie
        GdipAddPathPie.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathPolygon(GpPath *path, GDIPCONST GpPointF *points, INT count);
        GdipAddPathPolygon = gdiplus.GdipAddPathPolygon
        GdipAddPathPolygon.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathPath(GpPath *path, GDIPCONST GpPath* addingPath, BOOL connect);
        GdipAddPathPath = gdiplus.GdipAddPathPath
        GdipAddPathPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathString(GpPath *path, GDIPCONST WCHAR *string,
        # INT length, GDIPCONST GpFontFamily *family, INT style,
        # REAL emSize, GDIPCONST RectF *layoutRect,
        # GDIPCONST GpStringFormat *format);
        GdipAddPathString = gdiplus.GdipAddPathString
        GdipAddPathString.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathStringI(GpPath *path, GDIPCONST WCHAR *string,
        # INT length, GDIPCONST GpFontFamily *family, INT style,
        # REAL emSize, GDIPCONST Rect *layoutRect,
        # GDIPCONST GpStringFormat *format);
        GdipAddPathStringI = gdiplus.GdipAddPathStringI
        GdipAddPathStringI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathLineI(GpPath *path, INT x1, INT y1, INT x2, INT y2);
        GdipAddPathLineI = gdiplus.GdipAddPathLineI
        GdipAddPathLineI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathLine2I(GpPath *path, GDIPCONST GpPoint *points, INT count);
        GdipAddPathLine2I = gdiplus.GdipAddPathLine2I
        GdipAddPathLine2I.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathArcI(GpPath *path, INT x, INT y, INT width, INT height,
        # REAL startAngle, REAL sweepAngle);
        GdipAddPathArcI = gdiplus.GdipAddPathArcI
        GdipAddPathArcI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathBezierI(GpPath *path, INT x1, INT y1, INT x2, INT y2,
        # INT x3, INT y3, INT x4, INT y4);
        GdipAddPathBezierI = gdiplus.GdipAddPathBezierI
        GdipAddPathBezierI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathBeziersI(GpPath *path, GDIPCONST GpPoint *points, INT count);
        GdipAddPathBeziersI = gdiplus.GdipAddPathBeziersI
        GdipAddPathBeziersI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathCurveI(GpPath *path, GDIPCONST GpPoint *points, INT count);
        GdipAddPathCurveI = gdiplus.GdipAddPathCurveI
        GdipAddPathCurveI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathCurve2I(GpPath *path, GDIPCONST GpPoint *points, INT count,
        # REAL tension);
        GdipAddPathCurve2I = gdiplus.GdipAddPathCurve2I
        GdipAddPathCurve2I.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathCurve3I(GpPath *path, GDIPCONST GpPoint *points, INT count,
        # INT offset, INT numberOfSegments, REAL tension);
        GdipAddPathCurve3I = gdiplus.GdipAddPathCurve3I
        GdipAddPathCurve3I.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathClosedCurveI(GpPath *path, GDIPCONST GpPoint *points, INT count);
        GdipAddPathClosedCurveI = gdiplus.GdipAddPathClosedCurveI
        GdipAddPathClosedCurveI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathClosedCurve2I(GpPath *path, GDIPCONST GpPoint *points, INT count,
        # REAL tension);
        GdipAddPathClosedCurve2I = gdiplus.GdipAddPathClosedCurve2I
        GdipAddPathClosedCurve2I.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathRectangleI(GpPath *path, INT x, INT y, INT width, INT height);
        GdipAddPathRectangleI = gdiplus.GdipAddPathRectangleI
        GdipAddPathRectangleI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathRectanglesI(GpPath *path, GDIPCONST GpRect *rects, INT count);
        GdipAddPathRectanglesI = gdiplus.GdipAddPathRectanglesI
        GdipAddPathRectanglesI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathEllipseI(GpPath *path, INT x, INT y, INT width, INT height);
        GdipAddPathEllipseI = gdiplus.GdipAddPathEllipseI
        GdipAddPathEllipseI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathPieI(GpPath *path, INT x, INT y, INT width, INT height,
        # REAL startAngle, REAL sweepAngle);
        GdipAddPathPieI = gdiplus.GdipAddPathPieI
        GdipAddPathPieI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipAddPathPolygonI(GpPath *path, GDIPCONST GpPoint *points, INT count);
        GdipAddPathPolygonI = gdiplus.GdipAddPathPolygonI
        GdipAddPathPolygonI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipFlattenPath(GpPath *path, GpMatrix* matrix, REAL flatness);
        GdipFlattenPath = gdiplus.GdipFlattenPath
        GdipFlattenPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipWindingModeOutline(
        # GpPath *path,
        # GpMatrix *matrix,
        # REAL flatness
        # );
        GdipWindingModeOutline = gdiplus.GdipWindingModeOutline
        GdipWindingModeOutline.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipWidenPath(
        # GpPath *nativePath,
        # GpPen *pen,
        # GpMatrix *matrix,
        # REAL flatness
        # );
        GdipWidenPath = gdiplus.GdipWidenPath
        GdipWidenPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipWarpPath(GpPath *path, GpMatrix* matrix,
        # GDIPCONST GpPointF *points, INT count,
        # REAL srcx, REAL srcy, REAL srcwidth, REAL srcheight,
        # WarpMode warpMode, REAL flatness);
        GdipWarpPath = gdiplus.GdipWarpPath
        GdipWarpPath.restype = GpStatus

        # ------------------------------------------------------------------
        # PathIterator APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreatePathIter(GpPathIterator **iterator, GpPath* path);
        GdipCreatePathIter = gdiplus.GdipCreatePathIter
        GdipCreatePathIter.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeletePathIter(GpPathIterator *iterator);
        GdipDeletePathIter = gdiplus.GdipDeletePathIter
        GdipDeletePathIter.restype = GpStatus

        # ------------------------------------------------------------------
        # Matrix APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateMatrix(GpMatrix **matrix);
        GdipCreateMatrix = gdiplus.GdipCreateMatrix
        GdipCreateMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMatrix2(REAL m11, REAL m12, REAL m21, REAL m22, REAL dx,
        # REAL dy, GpMatrix **matrix);
        GdipCreateMatrix2 = gdiplus.GdipCreateMatrix2
        GdipCreateMatrix2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMatrix3(GDIPCONST GpRectF *rect, GDIPCONST GpPointF *dstplg,
        # GpMatrix **matrix);
        GdipCreateMatrix3 = gdiplus.GdipCreateMatrix3
        GdipCreateMatrix3.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMatrix3I(GDIPCONST GpRect *rect, GDIPCONST GpPoint *dstplg,
        # GpMatrix **matrix);
        GdipCreateMatrix3I = gdiplus.GdipCreateMatrix3I
        GdipCreateMatrix3I.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCloneMatrix(GpMatrix *matrix, GpMatrix **cloneMatrix);
        GdipCloneMatrix = gdiplus.GdipCloneMatrix
        GdipCloneMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeleteMatrix(GpMatrix *matrix);
        GdipDeleteMatrix = gdiplus.GdipDeleteMatrix
        GdipDeleteMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetMatrixElements(GpMatrix *matrix, REAL m11, REAL m12, REAL m21, REAL m22,
        # REAL dx, REAL dy);
        GdipSetMatrixElements = gdiplus.GdipSetMatrixElements
        GdipSetMatrixElements.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipMultiplyMatrix(GpMatrix *matrix, GpMatrix* matrix2,
        # GpMatrixOrder order);
        GdipMultiplyMatrix = gdiplus.GdipMultiplyMatrix
        GdipMultiplyMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTranslateMatrix(GpMatrix *matrix, REAL offsetX, REAL offsetY,
        # GpMatrixOrder order);
        GdipTranslateMatrix = gdiplus.GdipTranslateMatrix
        GdipTranslateMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipScaleMatrix(GpMatrix *matrix, REAL scaleX, REAL scaleY,
        # GpMatrixOrder order);
        GdipScaleMatrix = gdiplus.GdipScaleMatrix
        GdipScaleMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRotateMatrix(GpMatrix *matrix, REAL angle, GpMatrixOrder order);
        GdipRotateMatrix = gdiplus.GdipRotateMatrix
        GdipRotateMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipShearMatrix(GpMatrix *matrix, REAL shearX, REAL shearY,
        # GpMatrixOrder order);
        GdipShearMatrix = gdiplus.GdipShearMatrix
        GdipShearMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipInvertMatrix(GpMatrix *matrix);
        GdipInvertMatrix = gdiplus.GdipInvertMatrix
        GdipInvertMatrix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTransformMatrixPoints(GpMatrix *matrix, GpPointF *pts, INT count);
        GdipTransformMatrixPoints = gdiplus.GdipTransformMatrixPoints
        GdipTransformMatrixPoints.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTransformMatrixPointsI(GpMatrix *matrix, GpPoint *pts, INT count);
        GdipTransformMatrixPointsI = gdiplus.GdipTransformMatrixPointsI
        GdipTransformMatrixPointsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipVectorTransformMatrixPoints(GpMatrix *matrix, GpPointF *pts,
        # INT count);
        GdipVectorTransformMatrixPoints = (
            gdiplus.GdipVectorTransformMatrixPoints
        )
        GdipVectorTransformMatrixPoints.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipVectorTransformMatrixPointsI(GpMatrix *matrix, GpPoint *pts,
        # INT count);
        GdipVectorTransformMatrixPointsI = (
            gdiplus.GdipVectorTransformMatrixPointsI
        )
        GdipVectorTransformMatrixPointsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetMatrixElements(GDIPCONST GpMatrix *matrix, REAL *matrixOut);
        GdipGetMatrixElements = gdiplus.GdipGetMatrixElements
        GdipGetMatrixElements.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsMatrixInvertible(GDIPCONST GpMatrix *matrix, BOOL *result);
        GdipIsMatrixInvertible = gdiplus.GdipIsMatrixInvertible
        GdipIsMatrixInvertible.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsMatrixIdentity(GDIPCONST GpMatrix *matrix, BOOL *result);
        GdipIsMatrixIdentity = gdiplus.GdipIsMatrixIdentity
        GdipIsMatrixIdentity.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsMatrixEqual(GDIPCONST GpMatrix *matrix, GDIPCONST GpMatrix *matrix2,
        # BOOL *result);
        GdipIsMatrixEqual = gdiplus.GdipIsMatrixEqual
        GdipIsMatrixEqual.restype = GpStatus

        # ------------------------------------------------------------------
        # Region APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateRegion(GpRegion **region);
        GdipCreateRegion = gdiplus.GdipCreateRegion
        GdipCreateRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateRegionRect(GDIPCONST GpRectF *rect, GpRegion **region);
        GdipCreateRegionRect = gdiplus.GdipCreateRegionRect
        GdipCreateRegionRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateRegionRectI(GDIPCONST GpRect *rect, GpRegion **region);
        GdipCreateRegionRectI = gdiplus.GdipCreateRegionRectI
        GdipCreateRegionRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateRegionPath(GpPath *path, GpRegion **region);
        GdipCreateRegionPath = gdiplus.GdipCreateRegionPath
        GdipCreateRegionPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateRegionRgnData(GDIPCONST BYTE *regionData, INT size,
        # GpRegion **region);
        GdipCreateRegionRgnData = gdiplus.GdipCreateRegionRgnData
        GdipCreateRegionRgnData.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateRegionHrgn(HRGN hRgn, GpRegion **region);
        GdipCreateRegionHrgn = gdiplus.GdipCreateRegionHrgn
        GdipCreateRegionHrgn.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCloneRegion(GpRegion *region, GpRegion **cloneRegion);
        GdipCloneRegion = gdiplus.GdipCloneRegion
        GdipCloneRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeleteRegion(GpRegion *region);
        GdipDeleteRegion = gdiplus.GdipDeleteRegion
        GdipDeleteRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetInfinite(GpRegion *region);
        GdipSetInfinite = gdiplus.GdipSetInfinite
        GdipSetInfinite.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetEmpty(GpRegion *region);
        GdipSetEmpty = gdiplus.GdipSetEmpty
        GdipSetEmpty.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCombineRegionRect(GpRegion *region, GDIPCONST GpRectF *rect,
        # CombineMode combineMode);
        GdipCombineRegionRect = gdiplus.GdipCombineRegionRect
        GdipCombineRegionRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCombineRegionRectI(GpRegion *region, GDIPCONST GpRect *rect,
        # CombineMode combineMode);
        GdipCombineRegionRectI = gdiplus.GdipCombineRegionRectI
        GdipCombineRegionRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCombineRegionPath(GpRegion *region, GpPath *path, CombineMode combineMode);
        GdipCombineRegionPath = gdiplus.GdipCombineRegionPath
        GdipCombineRegionPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCombineRegionRegion(GpRegion *region,  GpRegion *region2,
        # CombineMode combineMode);
        GdipCombineRegionRegion = gdiplus.GdipCombineRegionRegion
        GdipCombineRegionRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTranslateRegion(GpRegion *region, REAL dx, REAL dy);
        GdipTranslateRegion = gdiplus.GdipTranslateRegion
        GdipTranslateRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTranslateRegionI(GpRegion *region, INT dx, INT dy);
        GdipTranslateRegionI = gdiplus.GdipTranslateRegionI
        GdipTranslateRegionI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTransformRegion(GpRegion *region, GpMatrix *matrix);
        GdipTransformRegion = gdiplus.GdipTransformRegion
        GdipTransformRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetRegionBounds(GpRegion *region, GpGraphics *graphics,
        # GpRectF *rect);
        GdipGetRegionBounds = gdiplus.GdipGetRegionBounds
        GdipGetRegionBounds.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetRegionBoundsI(GpRegion *region, GpGraphics *graphics,
        # GpRect *rect);
        GdipGetRegionBoundsI = gdiplus.GdipGetRegionBoundsI
        GdipGetRegionBoundsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetRegionHRgn(GpRegion *region, GpGraphics *graphics, HRGN *hRgn);
        GdipGetRegionHRgn = gdiplus.GdipGetRegionHRgn
        GdipGetRegionHRgn.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsEmptyRegion(GpRegion *region, GpGraphics *graphics,
        # BOOL *result);
        GdipIsEmptyRegion = gdiplus.GdipIsEmptyRegion
        GdipIsEmptyRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsInfiniteRegion(GpRegion *region, GpGraphics *graphics,
        # BOOL *result);
        GdipIsInfiniteRegion = gdiplus.GdipIsInfiniteRegion
        GdipIsInfiniteRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsEqualRegion(GpRegion *region, GpRegion *region2,
        # GpGraphics *graphics, BOOL *result);
        GdipIsEqualRegion = gdiplus.GdipIsEqualRegion
        GdipIsEqualRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetRegionDataSize(GpRegion *region, UINT * bufferSize);
        GdipGetRegionDataSize = gdiplus.GdipGetRegionDataSize
        GdipGetRegionDataSize.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisibleRegionPoint(GpRegion *region, REAL x, REAL y,
        # GpGraphics *graphics, BOOL *result);
        GdipIsVisibleRegionPoint = gdiplus.GdipIsVisibleRegionPoint
        GdipIsVisibleRegionPoint.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisibleRegionPointI(GpRegion *region, INT x, INT y,
        # GpGraphics *graphics, BOOL *result);
        GdipIsVisibleRegionPointI = gdiplus.GdipIsVisibleRegionPointI
        GdipIsVisibleRegionPointI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisibleRegionRect(GpRegion *region, REAL x, REAL y, REAL width,
        # REAL height, GpGraphics *graphics, BOOL *result);
        GdipIsVisibleRegionRect = gdiplus.GdipIsVisibleRegionRect
        GdipIsVisibleRegionRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisibleRegionRectI(GpRegion *region, INT x, INT y, INT width,
        # INT height, GpGraphics *graphics, BOOL *result);
        GdipIsVisibleRegionRectI = gdiplus.GdipIsVisibleRegionRectI
        GdipIsVisibleRegionRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetRegionScansCount(GpRegion *region, UINT* count, GpMatrix* matrix);
        GdipGetRegionScansCount = gdiplus.GdipGetRegionScansCount
        GdipGetRegionScansCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetRegionScans(GpRegion *region, GpRectF* rects, INT* count,
        # GpMatrix* matrix);
        GdipGetRegionScans = gdiplus.GdipGetRegionScans
        GdipGetRegionScans.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetRegionScansI(GpRegion *region, GpRect* rects, INT* count,
        # GpMatrix* matrix);
        GdipGetRegionScansI = gdiplus.GdipGetRegionScansI
        GdipGetRegionScansI.restype = GpStatus

        # ------------------------------------------------------------------
        # Brush APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCloneBrush(GpBrush *brush, GpBrush **cloneBrush);
        GdipCloneBrush = gdiplus.GdipCloneBrush
        GdipCloneBrush.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeleteBrush(GpBrush *brush);
        GdipDeleteBrush = gdiplus.GdipDeleteBrush
        GdipDeleteBrush.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetBrushType(GpBrush *brush, GpBrushType *type);
        GdipGetBrushType = gdiplus.GdipGetBrushType
        GdipGetBrushType.restype = GpStatus

        # ------------------------------------------------------------------
        # HatchBrush APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateHatchBrush(GpHatchStyle hatchstyle, ARGB forecol,
        # ARGB backcol, GpHatch **brush);
        GdipCreateHatchBrush = gdiplus.GdipCreateHatchBrush
        GdipCreateHatchBrush.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetHatchStyle(GpHatch *brush, GpHatchStyle *hatchstyle);
        GdipGetHatchStyle = gdiplus.GdipGetHatchStyle
        GdipGetHatchStyle.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetHatchForegroundColor(GpHatch *brush, ARGB* forecol);
        GdipGetHatchForegroundColor = gdiplus.GdipGetHatchForegroundColor
        GdipGetHatchForegroundColor.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetHatchBackgroundColor(GpHatch *brush, ARGB* backcol);
        GdipGetHatchBackgroundColor = gdiplus.GdipGetHatchBackgroundColor
        GdipGetHatchBackgroundColor.restype = GpStatus

        # ------------------------------------------------------------------
        # TextureBrush APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateTexture(GpImage *image, GpWrapMode wrapmode,
        # GpTexture **texture);
        GdipCreateTexture = gdiplus.GdipCreateTexture
        GdipCreateTexture.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateTexture2(GpImage *image, GpWrapMode wrapmode, REAL x,
        # REAL y, REAL width, REAL height, GpTexture **texture);
        GdipCreateTexture2 = gdiplus.GdipCreateTexture2
        GdipCreateTexture2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateTextureIA(GpImage *image,
        # GDIPCONST GpImageAttributes *imageAttributes,
        # REAL x, REAL y, REAL width, REAL height,
        # GpTexture **texture);
        GdipCreateTextureIA = gdiplus.GdipCreateTextureIA
        GdipCreateTextureIA.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateTexture2I(GpImage *image, GpWrapMode wrapmode, INT x,
        # INT y, INT width, INT height, GpTexture **texture);
        GdipCreateTexture2I = gdiplus.GdipCreateTexture2I
        GdipCreateTexture2I.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateTextureIAI(GpImage *image,
        # GDIPCONST GpImageAttributes *imageAttributes,
        # INT x, INT y, INT width, INT height,
        # GpTexture **texture);
        GdipCreateTextureIAI = gdiplus.GdipCreateTextureIAI
        GdipCreateTextureIAI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetTextureTransform(GpTexture *brush, GpMatrix *matrix);
        GdipGetTextureTransform = gdiplus.GdipGetTextureTransform
        GdipGetTextureTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetTextureTransform(GpTexture *brush, GDIPCONST GpMatrix *matrix);
        GdipSetTextureTransform = gdiplus.GdipSetTextureTransform
        GdipSetTextureTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetTextureWrapMode(GpTexture *brush, GpWrapMode wrapmode);
        GdipSetTextureWrapMode = gdiplus.GdipSetTextureWrapMode
        GdipSetTextureWrapMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetTextureWrapMode(GpTexture *brush, GpWrapMode *wrapmode);
        GdipGetTextureWrapMode = gdiplus.GdipGetTextureWrapMode
        GdipGetTextureWrapMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetTextureImage(GpTexture *brush, GpImage **image);
        GdipGetTextureImage = gdiplus.GdipGetTextureImage
        GdipGetTextureImage.restype = GpStatus

        # ------------------------------------------------------------------
        # SolidBrush APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateSolidFill(ARGB color, GpSolidFill **brush);
        GdipCreateSolidFill = gdiplus.GdipCreateSolidFill
        GdipCreateSolidFill.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetSolidFillColor(GpSolidFill *brush, ARGB color);
        GdipSetSolidFillColor = gdiplus.GdipSetSolidFillColor
        GdipSetSolidFillColor.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetSolidFillColor(GpSolidFill *brush, ARGB *color);
        GdipGetSolidFillColor = gdiplus.GdipGetSolidFillColor
        GdipGetSolidFillColor.restype = GpStatus

        # ------------------------------------------------------------------
        # LineBrush APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateLineBrush(GDIPCONST GpPointF* point1,
        # GDIPCONST GpPointF* point2,
        # ARGB color1, ARGB color2,
        # GpWrapMode wrapMode,
        # GpLineGradient **lineGradient);
        GdipCreateLineBrush = gdiplus.GdipCreateLineBrush
        GdipCreateLineBrush.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateLineBrushI(GDIPCONST GpPoint* point1,
        # GDIPCONST GpPoint* point2,
        # ARGB color1, ARGB color2,
        # GpWrapMode wrapMode,
        # GpLineGradient **lineGradient);
        GdipCreateLineBrushI = gdiplus.GdipCreateLineBrushI
        GdipCreateLineBrushI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateLineBrushFromRect(GDIPCONST GpRectF* rect,
        # ARGB color1, ARGB color2,
        # LinearGradientMode mode,
        # GpWrapMode wrapMode,
        # GpLineGradient **lineGradient);
        GdipCreateLineBrushFromRect = gdiplus.GdipCreateLineBrushFromRect
        GdipCreateLineBrushFromRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateLineBrushFromRectI(GDIPCONST GpRect* rect,
        # ARGB color1, ARGB color2,
        # LinearGradientMode mode,
        # GpWrapMode wrapMode,
        # GpLineGradient **lineGradient);
        GdipCreateLineBrushFromRectI = gdiplus.GdipCreateLineBrushFromRectI
        GdipCreateLineBrushFromRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateLineBrushFromRectWithAngle(GDIPCONST GpRectF* rect,
        # ARGB color1, ARGB color2,
        # REAL angle,
        # BOOL isAngleScalable,
        # GpWrapMode wrapMode,
        # GpLineGradient **lineGradient);
        GdipCreateLineBrushFromRectWithAngle = (
            gdiplus.GdipCreateLineBrushFromRectWithAngle
        )
        GdipCreateLineBrushFromRectWithAngle.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateLineBrushFromRectWithAngleI(GDIPCONST GpRect* rect,
        # ARGB color1, ARGB color2,
        # REAL angle,
        # BOOL isAngleScalable,
        # GpWrapMode wrapMode,
        # GpLineGradient **lineGradient);
        GdipCreateLineBrushFromRectWithAngleI = (
            gdiplus.GdipCreateLineBrushFromRectWithAngleI
        )
        GdipCreateLineBrushFromRectWithAngleI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLineColors(GpLineGradient *brush, ARGB color1, ARGB color2);
        GdipSetLineColors = gdiplus.GdipSetLineColors
        GdipSetLineColors.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineColors(GpLineGradient *brush, ARGB* colors);
        GdipGetLineColors = gdiplus.GdipGetLineColors
        GdipGetLineColors.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineRect(GpLineGradient *brush, GpRectF *rect);
        GdipGetLineRect = gdiplus.GdipGetLineRect
        GdipGetLineRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineRectI(GpLineGradient *brush, GpRect *rect);
        GdipGetLineRectI = gdiplus.GdipGetLineRectI
        GdipGetLineRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLineGammaCorrection(GpLineGradient *brush, BOOL useGammaCorrection);
        GdipSetLineGammaCorrection = gdiplus.GdipSetLineGammaCorrection
        GdipSetLineGammaCorrection.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineGammaCorrection(GpLineGradient *brush, BOOL *useGammaCorrection);
        GdipGetLineGammaCorrection = gdiplus.GdipGetLineGammaCorrection
        GdipGetLineGammaCorrection.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineBlendCount(GpLineGradient *brush, INT *count);
        GdipGetLineBlendCount = gdiplus.GdipGetLineBlendCount
        GdipGetLineBlendCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineBlend(GpLineGradient *brush, REAL *blend, REAL* positions,
        # INT count);
        GdipGetLineBlend = gdiplus.GdipGetLineBlend
        GdipGetLineBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLineBlend(GpLineGradient *brush, GDIPCONST REAL *blend,
        # GDIPCONST REAL* positions, INT count);
        GdipSetLineBlend = gdiplus.GdipSetLineBlend
        GdipSetLineBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLinePresetBlendCount(GpLineGradient *brush, INT *count);
        GdipGetLinePresetBlendCount = gdiplus.GdipGetLinePresetBlendCount
        GdipGetLinePresetBlendCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLinePresetBlend(GpLineGradient *brush, ARGB *blend,
        # REAL* positions, INT count);
        GdipGetLinePresetBlend = gdiplus.GdipGetLinePresetBlend
        GdipGetLinePresetBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLinePresetBlend(GpLineGradient *brush, GDIPCONST ARGB *blend,
        # GDIPCONST REAL* positions, INT count);
        GdipSetLinePresetBlend = gdiplus.GdipSetLinePresetBlend
        GdipSetLinePresetBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLineSigmaBlend(GpLineGradient *brush, REAL focus, REAL scale);
        GdipSetLineSigmaBlend = gdiplus.GdipSetLineSigmaBlend
        GdipSetLineSigmaBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLineLinearBlend(GpLineGradient *brush, REAL focus, REAL scale);
        GdipSetLineLinearBlend = gdiplus.GdipSetLineLinearBlend
        GdipSetLineLinearBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLineWrapMode(GpLineGradient *brush, GpWrapMode wrapmode);
        GdipSetLineWrapMode = gdiplus.GdipSetLineWrapMode
        GdipSetLineWrapMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineWrapMode(GpLineGradient *brush, GpWrapMode *wrapmode);
        GdipGetLineWrapMode = gdiplus.GdipGetLineWrapMode
        GdipGetLineWrapMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineTransform(GpLineGradient *brush, GpMatrix *matrix);
        GdipGetLineTransform = gdiplus.GdipGetLineTransform
        GdipGetLineTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetLineTransform(GpLineGradient *brush, GDIPCONST GpMatrix *matrix);
        GdipSetLineTransform = gdiplus.GdipSetLineTransform
        GdipSetLineTransform.restype = GpStatus

        # ------------------------------------------------------------------
        # PathGradientBrush APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreatePathGradient(GDIPCONST GpPointF* points,
        # INT count,
        # GpWrapMode wrapMode,
        # GpPathGradient **polyGradient);
        GdipCreatePathGradient = gdiplus.GdipCreatePathGradient
        GdipCreatePathGradient.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreatePathGradientI(GDIPCONST GpPoint* points,
        # INT count,
        # GpWrapMode wrapMode,
        # GpPathGradient **polyGradient);
        GdipCreatePathGradientI = gdiplus.GdipCreatePathGradientI
        GdipCreatePathGradientI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreatePathGradientFromPath(GDIPCONST GpPath* path,
        # GpPathGradient **polyGradient);
        GdipCreatePathGradientFromPath = gdiplus.GdipCreatePathGradientFromPath
        GdipCreatePathGradientFromPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientCenterColor(
        # GpPathGradient *brush, ARGB* colors);
        GdipGetPathGradientCenterColor = gdiplus.GdipGetPathGradientCenterColor
        GdipGetPathGradientCenterColor.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientCenterColor(
        # GpPathGradient *brush, ARGB colors);
        GdipSetPathGradientCenterColor = gdiplus.GdipSetPathGradientCenterColor
        GdipSetPathGradientCenterColor.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientSurroundColorsWithCount(
        # _In_ GpPathGradient *brush,
        # _Out_writes_to_(*count, *count) ARGB* color,
        # _Inout_ INT* count);
        GdipGetPathGradientSurroundColorsWithCount = (
            gdiplus.GdipGetPathGradientSurroundColorsWithCount
        )
        GdipGetPathGradientSurroundColorsWithCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientSurroundColorsWithCount(
        # GpPathGradient *brush,
        # GDIPCONST ARGB* color, INT* count);
        GdipSetPathGradientSurroundColorsWithCount = (
            gdiplus.GdipSetPathGradientSurroundColorsWithCount
        )
        GdipSetPathGradientSurroundColorsWithCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientPath(GpPathGradient *brush, GpPath *path);
        GdipGetPathGradientPath = gdiplus.GdipGetPathGradientPath
        GdipGetPathGradientPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientPath(GpPathGradient *brush, GDIPCONST GpPath *path);
        GdipSetPathGradientPath = gdiplus.GdipSetPathGradientPath
        GdipSetPathGradientPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientCenterPoint(
        # GpPathGradient *brush, GpPointF* points);
        GdipGetPathGradientCenterPoint = gdiplus.GdipGetPathGradientCenterPoint
        GdipGetPathGradientCenterPoint.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientCenterPointI(
        # GpPathGradient *brush, GpPoint* points);
        GdipGetPathGradientCenterPointI = (
            gdiplus.GdipGetPathGradientCenterPointI
        )
        GdipGetPathGradientCenterPointI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientCenterPoint(
        # GpPathGradient *brush, GDIPCONST GpPointF* points);
        GdipSetPathGradientCenterPoint = gdiplus.GdipSetPathGradientCenterPoint
        GdipSetPathGradientCenterPoint.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientCenterPointI(
        # GpPathGradient *brush, GDIPCONST GpPoint* points);
        GdipSetPathGradientCenterPointI = (
            gdiplus.GdipSetPathGradientCenterPointI
        )
        GdipSetPathGradientCenterPointI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientRect(GpPathGradient *brush, GpRectF *rect);
        GdipGetPathGradientRect = gdiplus.GdipGetPathGradientRect
        GdipGetPathGradientRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientRectI(GpPathGradient *brush, GpRect *rect);
        GdipGetPathGradientRectI = gdiplus.GdipGetPathGradientRectI
        GdipGetPathGradientRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientPointCount(GpPathGradient *brush, INT* count);
        GdipGetPathGradientPointCount = gdiplus.GdipGetPathGradientPointCount
        GdipGetPathGradientPointCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientSurroundColorCount(GpPathGradient *brush, INT* count);
        GdipGetPathGradientSurroundColorCount = (
            gdiplus.GdipGetPathGradientSurroundColorCount
        )
        GdipGetPathGradientSurroundColorCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientGammaCorrection(GpPathGradient *brush,
        # BOOL useGammaCorrection);
        GdipSetPathGradientGammaCorrection = (
            gdiplus.GdipSetPathGradientGammaCorrection
        )
        GdipSetPathGradientGammaCorrection.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientGammaCorrection(GpPathGradient *brush,
        # BOOL *useGammaCorrection);
        GdipGetPathGradientGammaCorrection = (
            gdiplus.GdipGetPathGradientGammaCorrection
        )
        GdipGetPathGradientGammaCorrection.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientBlendCount(GpPathGradient *brush,
        # INT *count);
        GdipGetPathGradientBlendCount = gdiplus.GdipGetPathGradientBlendCount
        GdipGetPathGradientBlendCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientBlend(GpPathGradient *brush,
        # REAL *blend, REAL *positions, INT count);
        GdipGetPathGradientBlend = gdiplus.GdipGetPathGradientBlend
        GdipGetPathGradientBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientBlend(GpPathGradient *brush,
        # GDIPCONST REAL *blend, GDIPCONST REAL *positions, INT count);
        GdipSetPathGradientBlend = gdiplus.GdipSetPathGradientBlend
        GdipSetPathGradientBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientPresetBlendCount(GpPathGradient *brush, INT *count);
        GdipGetPathGradientPresetBlendCount = (
            gdiplus.GdipGetPathGradientPresetBlendCount
        )
        GdipGetPathGradientPresetBlendCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientPresetBlend(GpPathGradient *brush, ARGB *blend,
        # REAL* positions, INT count);
        GdipGetPathGradientPresetBlend = gdiplus.GdipGetPathGradientPresetBlend
        GdipGetPathGradientPresetBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientPresetBlend(GpPathGradient *brush, GDIPCONST ARGB *blend,
        # GDIPCONST REAL* positions, INT count);
        GdipSetPathGradientPresetBlend = gdiplus.GdipSetPathGradientPresetBlend
        GdipSetPathGradientPresetBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientSigmaBlend(GpPathGradient *brush, REAL focus, REAL scale);
        GdipSetPathGradientSigmaBlend = gdiplus.GdipSetPathGradientSigmaBlend
        GdipSetPathGradientSigmaBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientLinearBlend(GpPathGradient *brush, REAL focus, REAL scale);
        GdipSetPathGradientLinearBlend = gdiplus.GdipSetPathGradientLinearBlend
        GdipSetPathGradientLinearBlend.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientWrapMode(GpPathGradient *brush,
        # GpWrapMode *wrapmode);
        GdipGetPathGradientWrapMode = gdiplus.GdipGetPathGradientWrapMode
        GdipGetPathGradientWrapMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientWrapMode(GpPathGradient *brush,
        # GpWrapMode wrapmode);
        GdipSetPathGradientWrapMode = gdiplus.GdipSetPathGradientWrapMode
        GdipSetPathGradientWrapMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientTransform(GpPathGradient *brush,
        # GpMatrix *matrix);
        GdipGetPathGradientTransform = gdiplus.GdipGetPathGradientTransform
        GdipGetPathGradientTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientTransform(GpPathGradient *brush,
        # GpMatrix *matrix);
        GdipSetPathGradientTransform = gdiplus.GdipSetPathGradientTransform
        GdipSetPathGradientTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPathGradientFocusScales(GpPathGradient *brush, REAL* xScale,
        # REAL* yScale);
        GdipGetPathGradientFocusScales = gdiplus.GdipGetPathGradientFocusScales
        GdipGetPathGradientFocusScales.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPathGradientFocusScales(GpPathGradient *brush, REAL xScale,
        # REAL yScale);
        GdipSetPathGradientFocusScales = gdiplus.GdipSetPathGradientFocusScales
        GdipSetPathGradientFocusScales.restype = GpStatus

        # ------------------------------------------------------------------
        # Pen APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreatePen1(ARGB color, REAL width, GpUnit unit, GpPen **pen);
        GdipCreatePen1 = gdiplus.GdipCreatePen1
        GdipCreatePen1.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreatePen2(GpBrush *brush, REAL width, GpUnit unit,
        # GpPen **pen);
        GdipCreatePen2 = gdiplus.GdipCreatePen2
        GdipCreatePen2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipClonePen(GpPen *pen, GpPen **clonepen);
        GdipClonePen = gdiplus.GdipClonePen
        GdipClonePen.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeletePen(GpPen *pen);
        GdipDeletePen = gdiplus.GdipDeletePen
        GdipDeletePen.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenWidth(GpPen *pen, REAL width);
        GdipSetPenWidth = gdiplus.GdipSetPenWidth
        GdipSetPenWidth.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenWidth(GpPen *pen, REAL *width);
        GdipGetPenWidth = gdiplus.GdipGetPenWidth
        GdipGetPenWidth.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenUnit(GpPen *pen, GpUnit unit);
        GdipSetPenUnit = gdiplus.GdipSetPenUnit
        GdipSetPenUnit.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenUnit(GpPen *pen, GpUnit *unit);
        GdipGetPenUnit = gdiplus.GdipGetPenUnit
        GdipGetPenUnit.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenLineCap197819(GpPen *pen, GpLineCap startCap, GpLineCap endCap,
        # GpDashCap dashCap);
        GdipSetPenLineCap197819 = gdiplus.GdipSetPenLineCap197819
        GdipSetPenLineCap197819.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenStartCap(GpPen *pen, GpLineCap startCap);
        GdipSetPenStartCap = gdiplus.GdipSetPenStartCap
        GdipSetPenStartCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenEndCap(GpPen *pen, GpLineCap endCap);
        GdipSetPenEndCap = gdiplus.GdipSetPenEndCap
        GdipSetPenEndCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenDashCap197819(GpPen *pen, GpDashCap dashCap);
        GdipSetPenDashCap197819 = gdiplus.GdipSetPenDashCap197819
        GdipSetPenDashCap197819.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenStartCap(GpPen *pen, GpLineCap *startCap);
        GdipGetPenStartCap = gdiplus.GdipGetPenStartCap
        GdipGetPenStartCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenEndCap(GpPen *pen, GpLineCap *endCap);
        GdipGetPenEndCap = gdiplus.GdipGetPenEndCap
        GdipGetPenEndCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenDashCap197819(GpPen *pen, GpDashCap *dashCap);
        GdipGetPenDashCap197819 = gdiplus.GdipGetPenDashCap197819
        GdipGetPenDashCap197819.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenLineJoin(GpPen *pen, GpLineJoin lineJoin);
        GdipSetPenLineJoin = gdiplus.GdipSetPenLineJoin
        GdipSetPenLineJoin.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenLineJoin(GpPen *pen, GpLineJoin *lineJoin);
        GdipGetPenLineJoin = gdiplus.GdipGetPenLineJoin
        GdipGetPenLineJoin.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenCustomStartCap(GpPen *pen, GpCustomLineCap* customCap);
        GdipSetPenCustomStartCap = gdiplus.GdipSetPenCustomStartCap
        GdipSetPenCustomStartCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenCustomStartCap(GpPen *pen, GpCustomLineCap** customCap);
        GdipGetPenCustomStartCap = gdiplus.GdipGetPenCustomStartCap
        GdipGetPenCustomStartCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenCustomEndCap(GpPen *pen, GpCustomLineCap* customCap);
        GdipSetPenCustomEndCap = gdiplus.GdipSetPenCustomEndCap
        GdipSetPenCustomEndCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenCustomEndCap(GpPen *pen, GpCustomLineCap** customCap);
        GdipGetPenCustomEndCap = gdiplus.GdipGetPenCustomEndCap
        GdipGetPenCustomEndCap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenMiterLimit(GpPen *pen, REAL miterLimit);
        GdipSetPenMiterLimit = gdiplus.GdipSetPenMiterLimit
        GdipSetPenMiterLimit.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenMiterLimit(GpPen *pen, REAL *miterLimit);
        GdipGetPenMiterLimit = gdiplus.GdipGetPenMiterLimit
        GdipGetPenMiterLimit.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenMode(GpPen *pen, GpPenAlignment penMode);
        GdipSetPenMode = gdiplus.GdipSetPenMode
        GdipSetPenMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenMode(GpPen *pen, GpPenAlignment *penMode);
        GdipGetPenMode = gdiplus.GdipGetPenMode
        GdipGetPenMode.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenTransform(GpPen *pen, GpMatrix *matrix);
        GdipSetPenTransform = gdiplus.GdipSetPenTransform
        GdipSetPenTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenTransform(GpPen *pen, GpMatrix *matrix);
        GdipGetPenTransform = gdiplus.GdipGetPenTransform
        GdipGetPenTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipResetPenTransform(GpPen *pen);
        GdipResetPenTransform = gdiplus.GdipResetPenTransform
        GdipResetPenTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipMultiplyPenTransform(GpPen *pen, GDIPCONST GpMatrix *matrix,
        # GpMatrixOrder order);
        GdipMultiplyPenTransform = gdiplus.GdipMultiplyPenTransform
        GdipMultiplyPenTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTranslatePenTransform(GpPen *pen, REAL dx, REAL dy,
        # GpMatrixOrder order);
        GdipTranslatePenTransform = gdiplus.GdipTranslatePenTransform
        GdipTranslatePenTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipScalePenTransform(GpPen *pen, REAL sx, REAL sy,
        # GpMatrixOrder order);
        GdipScalePenTransform = gdiplus.GdipScalePenTransform
        GdipScalePenTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRotatePenTransform(GpPen *pen, REAL angle, GpMatrixOrder order);
        GdipRotatePenTransform = gdiplus.GdipRotatePenTransform
        GdipRotatePenTransform.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenColor(GpPen *pen, ARGB argb);
        GdipSetPenColor = gdiplus.GdipSetPenColor
        GdipSetPenColor.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenColor(GpPen *pen, ARGB *argb);
        GdipGetPenColor = gdiplus.GdipGetPenColor
        GdipGetPenColor.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenBrushFill(GpPen *pen, GpBrush *brush);
        GdipSetPenBrushFill = gdiplus.GdipSetPenBrushFill
        GdipSetPenBrushFill.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenBrushFill(GpPen *pen, GpBrush **brush);
        GdipGetPenBrushFill = gdiplus.GdipGetPenBrushFill
        GdipGetPenBrushFill.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenFillType(GpPen *pen, GpPenType* type);
        GdipGetPenFillType = gdiplus.GdipGetPenFillType
        GdipGetPenFillType.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenDashStyle(GpPen *pen, GpDashStyle *dashstyle);
        GdipGetPenDashStyle = gdiplus.GdipGetPenDashStyle
        GdipGetPenDashStyle.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenDashStyle(GpPen *pen, GpDashStyle dashstyle);
        GdipSetPenDashStyle = gdiplus.GdipSetPenDashStyle
        GdipSetPenDashStyle.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenDashOffset(GpPen *pen, REAL *offset);
        GdipGetPenDashOffset = gdiplus.GdipGetPenDashOffset
        GdipGetPenDashOffset.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenDashOffset(GpPen *pen, REAL offset);
        GdipSetPenDashOffset = gdiplus.GdipSetPenDashOffset
        GdipSetPenDashOffset.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenDashCount(GpPen *pen, INT *count);
        GdipGetPenDashCount = gdiplus.GdipGetPenDashCount
        GdipGetPenDashCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenDashArray(GpPen *pen, GDIPCONST REAL *dash, INT count);
        GdipSetPenDashArray = gdiplus.GdipSetPenDashArray
        GdipSetPenDashArray.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenDashArray(GpPen *pen, REAL *dash, INT count);
        GdipGetPenDashArray = gdiplus.GdipGetPenDashArray
        GdipGetPenDashArray.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenCompoundCount(GpPen *pen, INT *count);
        GdipGetPenCompoundCount = gdiplus.GdipGetPenCompoundCount
        GdipGetPenCompoundCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPenCompoundArray(GpPen *pen, GDIPCONST REAL *dash, INT count);
        GdipSetPenCompoundArray = gdiplus.GdipSetPenCompoundArray
        GdipSetPenCompoundArray.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPenCompoundArray(GpPen *pen, REAL *dash, INT count);
        GdipGetPenCompoundArray = gdiplus.GdipGetPenCompoundArray
        GdipGetPenCompoundArray.restype = GpStatus

        # ------------------------------------------------------------------
        # CustomLineCap APIs
        # ------------------------------------------------------------------
        # ------------------------------------------------------------------
        # AdjustableArrowCap APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateAdjustableArrowCap(REAL height, REAL width, BOOL isFilled,
        # GpAdjustableArrowCap **cap);
        GdipCreateAdjustableArrowCap = gdiplus.GdipCreateAdjustableArrowCap
        GdipCreateAdjustableArrowCap.restype = GpStatus

        # ------------------------------------------------------------------
        # Image APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipLoadImageFromFile(GDIPCONST WCHAR* filename, GpImage **image);
        GdipLoadImageFromFile = gdiplus.GdipLoadImageFromFile
        GdipLoadImageFromFile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipLoadImageFromFileICM(GDIPCONST WCHAR* filename, GpImage **image);
        GdipLoadImageFromFileICM = gdiplus.GdipLoadImageFromFileICM
        GdipLoadImageFromFileICM.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCloneImage(GpImage *image, GpImage **cloneImage);
        GdipCloneImage = gdiplus.GdipCloneImage
        GdipCloneImage.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDisposeImage(GpImage *image);
        GdipDisposeImage = gdiplus.GdipDisposeImage
        GdipDisposeImage.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSaveImageToFile(GpImage *image, GDIPCONST WCHAR* filename,
        # GDIPCONST CLSID* clsidEncoder,
        # GDIPCONST EncoderParameters* encoderParams);
        GdipSaveImageToFile = gdiplus.GdipSaveImageToFile
        GdipSaveImageToFile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSaveImageToStream(GpImage *image, IStream* stream,
        # GDIPCONST CLSID* clsidEncoder,
        # GDIPCONST EncoderParameters* encoderParams);
        GdipSaveImageToStream = gdiplus.GdipSaveImageToStream
        GdipSaveImageToStream.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSaveAdd(GpImage *image, GDIPCONST EncoderParameters* encoderParams);
        GdipSaveAdd = gdiplus.GdipSaveAdd
        GdipSaveAdd.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSaveAddImage(GpImage *image, GpImage* newImage,
        # GDIPCONST EncoderParameters* encoderParams);
        GdipSaveAddImage = gdiplus.GdipSaveAddImage
        GdipSaveAddImage.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageGraphicsContext(GpImage *image, GpGraphics **graphics);
        GdipGetImageGraphicsContext = gdiplus.GdipGetImageGraphicsContext
        GdipGetImageGraphicsContext.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageBounds(GpImage *image, GpRectF *srcRect, GpUnit *srcUnit);
        GdipGetImageBounds = gdiplus.GdipGetImageBounds
        GdipGetImageBounds.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageDimension(GpImage *image, REAL *width, REAL *height);
        GdipGetImageDimension = gdiplus.GdipGetImageDimension
        GdipGetImageDimension.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageType(GpImage *image, ImageType *type);
        GdipGetImageType = gdiplus.GdipGetImageType
        GdipGetImageType.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageWidth(GpImage *image, UINT *width);
        GdipGetImageWidth = gdiplus.GdipGetImageWidth
        GdipGetImageWidth.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageHeight(GpImage *image, UINT *height);
        GdipGetImageHeight = gdiplus.GdipGetImageHeight
        GdipGetImageHeight.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageHorizontalResolution(GpImage *image, REAL *resolution);
        GdipGetImageHorizontalResolution = (
            gdiplus.GdipGetImageHorizontalResolution
        )
        GdipGetImageHorizontalResolution.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageVerticalResolution(GpImage *image, REAL *resolution);
        GdipGetImageVerticalResolution = gdiplus.GdipGetImageVerticalResolution
        GdipGetImageVerticalResolution.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageFlags(GpImage *image, UINT *flags);
        GdipGetImageFlags = gdiplus.GdipGetImageFlags
        GdipGetImageFlags.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageRawFormat(GpImage *image, GUID *format);
        GdipGetImageRawFormat = gdiplus.GdipGetImageRawFormat
        GdipGetImageRawFormat.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImagePixelFormat(GpImage *image, PixelFormat *format);
        GdipGetImagePixelFormat = gdiplus.GdipGetImagePixelFormat
        GdipGetImagePixelFormat.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageThumbnail(GpImage *image, UINT thumbWidth, UINT thumbHeight,
        # GpImage **thumbImage,
        # GetThumbnailImageAbort callback, VOID * callbackData);
        GdipGetImageThumbnail = gdiplus.GdipGetImageThumbnail
        GdipGetImageThumbnail.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetEncoderParameterListSize(GpImage *image, GDIPCONST CLSID* clsidEncoder,
        # UINT* size);
        GdipGetEncoderParameterListSize = (
            gdiplus.GdipGetEncoderParameterListSize
        )
        GdipGetEncoderParameterListSize.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetEncoderParameterList(GpImage *image, GDIPCONST CLSID* clsidEncoder,
        # UINT size, EncoderParameters* buffer);
        GdipGetEncoderParameterList = gdiplus.GdipGetEncoderParameterList
        GdipGetEncoderParameterList.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipImageGetFrameCount(GpImage *image, GDIPCONST GUID* dimensionID,
        # UINT* count);
        GdipImageGetFrameCount = gdiplus.GdipImageGetFrameCount
        GdipImageGetFrameCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipImageSelectActiveFrame(GpImage *image, GDIPCONST GUID* dimensionID,
        # UINT frameIndex);
        GdipImageSelectActiveFrame = gdiplus.GdipImageSelectActiveFrame
        GdipImageSelectActiveFrame.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipImageRotateFlip(GpImage *image, RotateFlipType rfType);
        GdipImageRotateFlip = gdiplus.GdipImageRotateFlip
        GdipImageRotateFlip.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImagePalette(GpImage *image, ColorPalette *palette, INT size);
        GdipGetImagePalette = gdiplus.GdipGetImagePalette
        GdipGetImagePalette.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetImagePalette(GpImage *image, GDIPCONST ColorPalette *palette);
        GdipSetImagePalette = gdiplus.GdipSetImagePalette
        GdipSetImagePalette.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImagePaletteSize(GpImage *image, INT *size);
        GdipGetImagePaletteSize = gdiplus.GdipGetImagePaletteSize
        GdipGetImagePaletteSize.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPropertyCount(GpImage *image, UINT* numOfProperty);
        GdipGetPropertyCount = gdiplus.GdipGetPropertyCount
        GdipGetPropertyCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPropertyIdList(GpImage *image, UINT numOfProperty, PROPID* list);
        GdipGetPropertyIdList = gdiplus.GdipGetPropertyIdList
        GdipGetPropertyIdList.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPropertyItemSize(GpImage *image, PROPID propId, UINT* size);
        GdipGetPropertyItemSize = gdiplus.GdipGetPropertyItemSize
        GdipGetPropertyItemSize.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPropertyItem(GpImage *image, PROPID propId,UINT propSize,
        # PropertyItem* buffer);
        GdipGetPropertyItem = gdiplus.GdipGetPropertyItem
        GdipGetPropertyItem.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetPropertySize(GpImage *image, UINT* totalBufferSize,
        # UINT* numProperties);
        GdipGetPropertySize = gdiplus.GdipGetPropertySize
        GdipGetPropertySize.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetAllPropertyItems(GpImage *image, UINT totalBufferSize,
        # UINT numProperties, PropertyItem* allItems);
        GdipGetAllPropertyItems = gdiplus.GdipGetAllPropertyItems
        GdipGetAllPropertyItems.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRemovePropertyItem(GpImage *image, PROPID propId);
        GdipRemovePropertyItem = gdiplus.GdipRemovePropertyItem
        GdipRemovePropertyItem.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetPropertyItem(GpImage *image, GDIPCONST PropertyItem* item);
        GdipSetPropertyItem = gdiplus.GdipSetPropertyItem
        GdipSetPropertyItem.restype = GpStatus

        if GDIPVER >= 0x0110:
            # GpStatus WINGDIPAPI
            # GdipFindFirstImageItem(GpImage *image, ImageItemData* item);
            GdipFindFirstImageItem = gdiplus.GdipFindFirstImageItem
            GdipFindFirstImageItem.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipFindNextImageItem(GpImage *image, ImageItemData* item);
            GdipFindNextImageItem = gdiplus.GdipFindNextImageItem
            GdipFindNextImageItem.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipGetImageItemData(GpImage *image, ImageItemData* item);
            GdipGetImageItemData = gdiplus.GdipGetImageItemData
            GdipGetImageItemData.restype = GpStatus

        # END IF  (GDIPVER >= 0x0110)

        # GpStatus WINGDIPAPI
        # GdipImageForceValidation(GpImage *image);
        GdipImageForceValidation = gdiplus.GdipImageForceValidation
        GdipImageForceValidation.restype = GpStatus

        # ------------------------------------------------------------------
        # Bitmap APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateBitmapFromFile(GDIPCONST WCHAR* filename, GpBitmap **bitmap);
        GdipCreateBitmapFromFile = gdiplus.GdipCreateBitmapFromFile
        GdipCreateBitmapFromFile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateBitmapFromFileICM(GDIPCONST WCHAR* filename, GpBitmap **bitmap);
        GdipCreateBitmapFromFileICM = gdiplus.GdipCreateBitmapFromFileICM
        GdipCreateBitmapFromFileICM.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateBitmapFromGraphics(INT width,
        # INT height,
        # GpGraphics* target,
        # GpBitmap** bitmap);
        GdipCreateBitmapFromGraphics = gdiplus.GdipCreateBitmapFromGraphics
        GdipCreateBitmapFromGraphics.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateBitmapFromGdiDib(GDIPCONST BITMAPINFO* gdiBitmapInfo,
        # VOID* gdiBitmapData,
        # GpBitmap** bitmap);
        GdipCreateBitmapFromGdiDib = gdiplus.GdipCreateBitmapFromGdiDib
        GdipCreateBitmapFromGdiDib.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateBitmapFromHBITMAP(HBITMAP hbm,
        # HPALETTE hpal,
        # GpBitmap** bitmap);
        GdipCreateBitmapFromHBITMAP = gdiplus.GdipCreateBitmapFromHBITMAP
        GdipCreateBitmapFromHBITMAP.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateBitmapFromHICON(HICON hicon,
        # GpBitmap** bitmap);
        GdipCreateBitmapFromHICON = gdiplus.GdipCreateBitmapFromHICON
        GdipCreateBitmapFromHICON.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateBitmapFromResource(HINSTANCE hInstance,
        # GDIPCONST WCHAR* lpBitmapName,
        # GpBitmap** bitmap);
        GdipCreateBitmapFromResource = gdiplus.GdipCreateBitmapFromResource
        GdipCreateBitmapFromResource.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCloneBitmapArea(REAL x, REAL y, REAL width, REAL height,
        # PixelFormat format,
        # GpBitmap *srcBitmap,
        # GpBitmap **dstBitmap);
        GdipCloneBitmapArea = gdiplus.GdipCloneBitmapArea
        GdipCloneBitmapArea.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCloneBitmapAreaI(INT x,
        # INT y,
        # INT width,
        # INT height,
        # PixelFormat format,
        # GpBitmap *srcBitmap,
        # GpBitmap **dstBitmap);
        GdipCloneBitmapAreaI = gdiplus.GdipCloneBitmapAreaI
        GdipCloneBitmapAreaI.restype = GpStatus

        if GDIPVER >= 0x0110:
            # GpStatus WINGDIPAPI GdipImageSetAbort(
            # GpImage *pImage,
            # GdiplusAbort *pIAbort
            # );
            GdipImageSetAbort = gdiplus.GdipImageSetAbort
            GdipImageSetAbort.restype = GpStatus

            # GpStatus WINGDIPAPI GdipGraphicsSetAbort(
            # GpGraphics *pGraphics,
            # GdiplusAbort *pIAbort
            # );
            GdipGraphicsSetAbort = gdiplus.GdipGraphicsSetAbort
            GdipGraphicsSetAbort.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipBitmapConvertFormat(
            # IN GpBitmap *pInputBitmap,
            # PixelFormat format,
            # DitherType dithertype,
            # PaletteType palettetype,
            # ColorPalette *palette,
            # REAL alphaThresholdPercent
            # );
            GdipBitmapConvertFormat = gdiplus.GdipBitmapConvertFormat
            GdipBitmapConvertFormat.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipInitializePalette(
            # OUT ColorPalette *palette, // output palette. must be allocated.
            # PaletteType palettetype, // palette enumeration type.
            # INT optimalColors, // how many optimal colors
            # BOOL useTransparentColor, // add a transparent color to the palette.
            # GpBitmap *bitmap // optional bitmap for median cut.
            # );
            GdipInitializePalette = gdiplus.GdipInitializePalette
            GdipInitializePalette.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipBitmapApplyEffect(
            # GpBitmap* bitmap,
            # CGpEffect *effect,
            # RECT *roi,
            # BOOL useAuxData,
            # VOID **auxData,
            # INT *auxDataSize
            # );
            GdipBitmapApplyEffect = gdiplus.GdipBitmapApplyEffect
            GdipBitmapApplyEffect.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipBitmapCreateApplyEffect(
            # GpBitmap **inputBitmaps,
            # INT numInputs,
            # CGpEffect *effect,
            # RECT *roi,
            # RECT *outputRect,
            # GpBitmap **outputBitmap,
            # BOOL useAuxData,
            # VOID **auxData,
            # INT *auxDataSize
            # );
            GdipBitmapCreateApplyEffect = gdiplus.GdipBitmapCreateApplyEffect
            GdipBitmapCreateApplyEffect.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipBitmapGetHistogram(
            # GpBitmap* bitmap,
            # IN HistogramFormat format,
            # IN UINT NumberOfEntries,
            # _Out_writes_bytes_((ctypes.sizeof(UINT)*256) UINT *channel0,
            # _Out_writes_bytes_((ctypes.sizeof(UINT)*256) UINT *channel1,
            # _Out_writes_bytes_((ctypes.sizeof(UINT)*256) UINT *channel2,
            # _Out_writes_bytes_((ctypes.sizeof(UINT)*256) UINT *channel3
            # );
            GdipBitmapGetHistogram = gdiplus.GdipBitmapGetHistogram
            GdipBitmapGetHistogram.restype = GpStatus
            # GpStatus WINGDIPAPI
            # GdipBitmapGetHistogramSize(
            # IN HistogramFormat format,
            # OUT UINT *NumberOfEntries
            # );
            GdipBitmapGetHistogramSize = gdiplus.GdipBitmapGetHistogramSize
            GdipBitmapGetHistogramSize.restype = GpStatus
        # END IF
        # ------------------------------------------------------------------
        # ImageAttributes APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateImageAttributes(GpImageAttributes **imageattr);
        GdipCreateImageAttributes = gdiplus.GdipCreateImageAttributes
        GdipCreateImageAttributes.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipCloneImageAttributes(GDIPCONST GpImageAttributes *imageattr,
        # GpImageAttributes **cloneImageattr);
        GdipCloneImageAttributes = gdiplus.GdipCloneImageAttributes
        GdipCloneImageAttributes.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDisposeImageAttributes(GpImageAttributes *imageattr);
        GdipDisposeImageAttributes = gdiplus.GdipDisposeImageAttributes
        GdipDisposeImageAttributes.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesToIdentity(GpImageAttributes *imageattr,
        # ColorAdjustType type);
        GdipSetImageAttributesToIdentity = (
            gdiplus.GdipSetImageAttributesToIdentity
        )
        GdipSetImageAttributesToIdentity.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipResetImageAttributes(GpImageAttributes *imageattr,
        # ColorAdjustType type);
        GdipResetImageAttributes = gdiplus.GdipResetImageAttributes
        GdipResetImageAttributes.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesColorMatrix(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag,
        # GDIPCONST ColorMatrix* colorMatrix,
        # GDIPCONST ColorMatrix* grayMatrix,
        # ColorMatrixFlags flags);
        GdipSetImageAttributesColorMatrix = (
            gdiplus.GdipSetImageAttributesColorMatrix
        )
        GdipSetImageAttributesColorMatrix.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesThreshold(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag,
        # REAL threshold);
        GdipSetImageAttributesThreshold = (
            gdiplus.GdipSetImageAttributesThreshold
        )
        GdipSetImageAttributesThreshold.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesGamma(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag,
        # REAL gamma);
        GdipSetImageAttributesGamma = gdiplus.GdipSetImageAttributesGamma
        GdipSetImageAttributesGamma.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesNoOp(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag);
        GdipSetImageAttributesNoOp = gdiplus.GdipSetImageAttributesNoOp
        GdipSetImageAttributesNoOp.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesColorKeys(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag,
        # ARGB colorLow,
        # ARGB colorHigh);
        GdipSetImageAttributesColorKeys = (
            gdiplus.GdipSetImageAttributesColorKeys
        )
        GdipSetImageAttributesColorKeys.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesOutputChannel(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag,
        # ColorChannelFlags channelFlags);
        GdipSetImageAttributesOutputChannel = (
            gdiplus.GdipSetImageAttributesOutputChannel
        )
        GdipSetImageAttributesOutputChannel.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesOutputChannelColorProfile(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag,
        # GDIPCONST
        # WCHAR *colorProfileFilename);
        GdipSetImageAttributesOutputChannelColorProfile = (
            gdiplus.GdipSetImageAttributesOutputChannelColorProfile
        )
        GdipSetImageAttributesOutputChannelColorProfile.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesRemapTable(GpImageAttributes *imageattr,
        # ColorAdjustType type,
        # BOOL enableFlag,
        # UINT mapSize,
        # GDIPCONST ColorMap *map);
        GdipSetImageAttributesRemapTable = (
            gdiplus.GdipSetImageAttributesRemapTable
        )
        GdipSetImageAttributesRemapTable.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesWrapMode(
        # GpImageAttributes *imageAttr,
        # WrapMode wrap,
        # ARGB argb,
        # BOOL clamp
        # );
        GdipSetImageAttributesWrapMode = gdiplus.GdipSetImageAttributesWrapMode
        GdipSetImageAttributesWrapMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesICMMode(
        # GpImageAttributes *imageAttr,
        # BOOL on
        # );
        GdipSetImageAttributesICMMode = gdiplus.GdipSetImageAttributesICMMode
        GdipSetImageAttributesICMMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetImageAttributesAdjustedPalette(
        # GpImageAttributes *imageAttr,
        # ColorPalette * colorPalette,
        # ColorAdjustType colorAdjustType
        # );
        GdipGetImageAttributesAdjustedPalette = (
            gdiplus.GdipGetImageAttributesAdjustedPalette
        )
        GdipGetImageAttributesAdjustedPalette.restype = GpStatus
        # ------------------------------------------------------------------
        # Graphics APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipFlush(GpGraphics *graphics, GpFlushIntention intention);
        GdipFlush = gdiplus.GdipFlush
        GdipFlush.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipCreateFromHDC(HDC hdc, GpGraphics **graphics);
        GdipCreateFromHDC = gdiplus.GdipCreateFromHDC
        GdipCreateFromHDC.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipCreateFromHDC2(HDC hdc, HANDLE hDevice, GpGraphics **graphics);
        GdipCreateFromHDC2 = gdiplus.GdipCreateFromHDC2
        GdipCreateFromHDC2.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipCreateFromHWND(HWND hwnd, GpGraphics **graphics);
        GdipCreateFromHWND = gdiplus.GdipCreateFromHWND
        GdipCreateFromHWND.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipCreateFromHWNDICM(HWND hwnd, GpGraphics **graphics);
        GdipCreateFromHWNDICM = gdiplus.GdipCreateFromHWNDICM
        GdipCreateFromHWNDICM.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDeleteGraphics(GpGraphics *graphics);
        GdipDeleteGraphics = gdiplus.GdipDeleteGraphics
        GdipDeleteGraphics.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetCompositingMode(GpGraphics *graphics, CompositingMode compositingMode);
        GdipSetCompositingMode = gdiplus.GdipSetCompositingMode
        GdipSetCompositingMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetCompositingMode(GpGraphics *graphics, CompositingMode *compositingMode);
        GdipGetCompositingMode = gdiplus.GdipGetCompositingMode
        GdipGetCompositingMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetRenderingOrigin(GpGraphics *graphics, INT x, INT y);
        GdipSetRenderingOrigin = gdiplus.GdipSetRenderingOrigin
        GdipSetRenderingOrigin.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetRenderingOrigin(GpGraphics *graphics, INT *x, INT *y);
        GdipGetRenderingOrigin = gdiplus.GdipGetRenderingOrigin
        GdipGetRenderingOrigin.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetCompositingQuality(GpGraphics *graphics,
        # CompositingQuality compositingQuality);
        GdipSetCompositingQuality = gdiplus.GdipSetCompositingQuality
        GdipSetCompositingQuality.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetCompositingQuality(GpGraphics *graphics,
        # CompositingQuality *compositingQuality);
        GdipGetCompositingQuality = gdiplus.GdipGetCompositingQuality
        GdipGetCompositingQuality.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetSmoothingMode(GpGraphics *graphics, SmoothingMode smoothingMode);
        GdipSetSmoothingMode = gdiplus.GdipSetSmoothingMode
        GdipSetSmoothingMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetSmoothingMode(GpGraphics *graphics, SmoothingMode *smoothingMode);
        GdipGetSmoothingMode = gdiplus.GdipGetSmoothingMode
        GdipGetSmoothingMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetPixelOffsetMode(GpGraphics *graphics, PixelOffsetMode *pixelOffsetMode);
        GdipGetPixelOffsetMode = gdiplus.GdipGetPixelOffsetMode
        GdipGetPixelOffsetMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetTextRenderingHint(GpGraphics *graphics, TextRenderingHint mode);
        GdipSetTextRenderingHint = gdiplus.GdipSetTextRenderingHint
        GdipSetTextRenderingHint.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetTextRenderingHint(GpGraphics *graphics, TextRenderingHint *mode);
        GdipGetTextRenderingHint = gdiplus.GdipGetTextRenderingHint
        GdipGetTextRenderingHint.restype = GpStatus
        # GpStatus  WINGDIPAPI
        # GdipSetTextContrast(GpGraphics *graphics, UINT contrast);
        GdipSetTextContrast = gdiplus.GdipSetTextContrast
        GdipSetTextContrast.restype = GpStatus
        # GpStatus  WINGDIPAPI
        # GdipGetTextContrast(GpGraphics *graphics, UINT * contrast);
        GdipGetTextContrast = gdiplus.GdipGetTextContrast
        GdipGetTextContrast.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetInterpolationMode(GpGraphics *graphics,
        # InterpolationMode interpolationMode);
        GdipSetInterpolationMode = gdiplus.GdipSetInterpolationMode
        GdipSetInterpolationMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetInterpolationMode(GpGraphics *graphics,
        # InterpolationMode *interpolationMode);
        GdipGetInterpolationMode = gdiplus.GdipGetInterpolationMode
        GdipGetInterpolationMode.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetWorldTransform(GpGraphics *graphics, GpMatrix *matrix);
        GdipSetWorldTransform = gdiplus.GdipSetWorldTransform
        GdipSetWorldTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipResetWorldTransform(GpGraphics *graphics);
        GdipResetWorldTransform = gdiplus.GdipResetWorldTransform
        GdipResetWorldTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipMultiplyWorldTransform(GpGraphics *graphics, GDIPCONST GpMatrix *matrix,
        # GpMatrixOrder order);
        GdipMultiplyWorldTransform = gdiplus.GdipMultiplyWorldTransform
        GdipMultiplyWorldTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipTranslateWorldTransform(GpGraphics *graphics, REAL dx, REAL dy,
        # GpMatrixOrder order);
        GdipTranslateWorldTransform = gdiplus.GdipTranslateWorldTransform
        GdipTranslateWorldTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipScaleWorldTransform(GpGraphics *graphics, REAL sx, REAL sy,
        # GpMatrixOrder order);
        GdipScaleWorldTransform = gdiplus.GdipScaleWorldTransform
        GdipScaleWorldTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipRotateWorldTransform(GpGraphics *graphics, REAL angle,
        # GpMatrixOrder order);
        GdipRotateWorldTransform = gdiplus.GdipRotateWorldTransform
        GdipRotateWorldTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetWorldTransform(GpGraphics *graphics, GpMatrix *matrix);
        GdipGetWorldTransform = gdiplus.GdipGetWorldTransform
        GdipGetWorldTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipResetPageTransform(GpGraphics *graphics);
        GdipResetPageTransform = gdiplus.GdipResetPageTransform
        GdipResetPageTransform.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetPageUnit(GpGraphics *graphics, GpUnit *unit);
        GdipGetPageUnit = gdiplus.GdipGetPageUnit
        GdipGetPageUnit.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetPageScale(GpGraphics *graphics, REAL *scale);
        GdipGetPageScale = gdiplus.GdipGetPageScale
        GdipGetPageScale.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetPageUnit(GpGraphics *graphics, GpUnit unit);
        GdipSetPageUnit = gdiplus.GdipSetPageUnit
        GdipSetPageUnit.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipSetPageScale(GpGraphics *graphics, REAL scale);
        GdipSetPageScale = gdiplus.GdipSetPageScale
        GdipSetPageScale.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetDpiX(GpGraphics *graphics, REAL* dpi);
        GdipGetDpiX = gdiplus.GdipGetDpiX
        GdipGetDpiX.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetDpiY(GpGraphics *graphics, REAL* dpi);
        GdipGetDpiY = gdiplus.GdipGetDpiY
        GdipGetDpiY.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipTransformPoints(GpGraphics *graphics, GpCoordinateSpace destSpace,
        # GpCoordinateSpace srcSpace, GpPointF *points,
        # INT count);
        GdipTransformPoints = gdiplus.GdipTransformPoints
        GdipTransformPoints.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipTransformPointsI(GpGraphics *graphics, GpCoordinateSpace destSpace,
        # GpCoordinateSpace srcSpace, GpPoint *points,
        # INT count);
        GdipTransformPointsI = gdiplus.GdipTransformPointsI
        GdipTransformPointsI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGetNearestColor(GpGraphics *graphics, ARGB* argb);
        GdipGetNearestColor = gdiplus.GdipGetNearestColor
        GdipGetNearestColor.restype = GpStatus
        # Creates the Win9x Halftone Palette (even on NT) with correct Desktop
        # colors        # GpStatus WINGDIPAPI
        # GdipDrawLine(GpGraphics *graphics, GpPen *pen, REAL x1, REAL y1,
        # REAL x2, REAL y2);
        GdipDrawLine = gdiplus.GdipDrawLine
        GdipDrawLine.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawLineI(GpGraphics *graphics, GpPen *pen, INT x1, INT y1,
        # INT x2, INT y2);
        GdipDrawLineI = gdiplus.GdipDrawLineI
        GdipDrawLineI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawLines(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points,
        # INT count);
        GdipDrawLines = gdiplus.GdipDrawLines
        GdipDrawLines.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawLinesI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points,
        # INT count);
        GdipDrawLinesI = gdiplus.GdipDrawLinesI
        GdipDrawLinesI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawArc(GpGraphics *graphics, GpPen *pen, REAL x, REAL y,
        # REAL width, REAL height, REAL startAngle, REAL sweepAngle);
        GdipDrawArc = gdiplus.GdipDrawArc
        GdipDrawArc.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawArcI(GpGraphics *graphics, GpPen *pen, INT x, INT y,
        # INT width, INT height, REAL startAngle, REAL sweepAngle);
        GdipDrawArcI = gdiplus.GdipDrawArcI
        GdipDrawArcI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawBezier(GpGraphics *graphics, GpPen *pen, REAL x1, REAL y1,
        # REAL x2, REAL y2, REAL x3, REAL y3, REAL x4, REAL y4);
        GdipDrawBezier = gdiplus.GdipDrawBezier
        GdipDrawBezier.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawBezierI(GpGraphics *graphics, GpPen *pen, INT x1, INT y1,
        # INT x2, INT y2, INT x3, INT y3, INT x4, INT y4);
        GdipDrawBezierI = gdiplus.GdipDrawBezierI
        GdipDrawBezierI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawBeziers(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points,
        # INT count);
        GdipDrawBeziers = gdiplus.GdipDrawBeziers
        GdipDrawBeziers.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawBeziersI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points,
        # INT count);
        GdipDrawBeziersI = gdiplus.GdipDrawBeziersI
        GdipDrawBeziersI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawRectangle(GpGraphics *graphics, GpPen *pen, REAL x, REAL y,
        # REAL width, REAL height);
        GdipDrawRectangle = gdiplus.GdipDrawRectangle
        GdipDrawRectangle.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawRectangleI(GpGraphics *graphics, GpPen *pen, INT x, INT y,
        # INT width, INT height);
        GdipDrawRectangleI = gdiplus.GdipDrawRectangleI
        GdipDrawRectangleI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawRectangles(GpGraphics *graphics, GpPen *pen, GDIPCONST GpRectF *rects,
        # INT count);
        GdipDrawRectangles = gdiplus.GdipDrawRectangles
        GdipDrawRectangles.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawRectanglesI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpRect *rects,
        # INT count);
        GdipDrawRectanglesI = gdiplus.GdipDrawRectanglesI
        GdipDrawRectanglesI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawEllipse(GpGraphics *graphics, GpPen *pen, REAL x, REAL y,
        # REAL width, REAL height);
        GdipDrawEllipse = gdiplus.GdipDrawEllipse
        GdipDrawEllipse.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawEllipseI(GpGraphics *graphics, GpPen *pen, INT x, INT y,
        # INT width, INT height);
        GdipDrawEllipseI = gdiplus.GdipDrawEllipseI
        GdipDrawEllipseI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawPie(GpGraphics *graphics, GpPen *pen, REAL x, REAL y,
        # REAL width, REAL height, REAL startAngle,
        # REAL sweepAngle);
        GdipDrawPie = gdiplus.GdipDrawPie
        GdipDrawPie.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawPieI(GpGraphics *graphics, GpPen *pen, INT x, INT y,
        # INT width, INT height, REAL startAngle, REAL sweepAngle);
        GdipDrawPieI = gdiplus.GdipDrawPieI
        GdipDrawPieI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawPolygon(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points,
        # INT count);
        GdipDrawPolygon = gdiplus.GdipDrawPolygon
        GdipDrawPolygon.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawPolygonI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points,
        # INT count);
        GdipDrawPolygonI = gdiplus.GdipDrawPolygonI
        GdipDrawPolygonI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawPath(GpGraphics *graphics, GpPen *pen, GpPath *path);
        GdipDrawPath = gdiplus.GdipDrawPath
        GdipDrawPath.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawCurve(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points,
        # INT count);
        GdipDrawCurve = gdiplus.GdipDrawCurve
        GdipDrawCurve.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawCurveI(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points,
        # INT count);
        GdipDrawCurveI = gdiplus.GdipDrawCurveI
        GdipDrawCurveI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawCurve2(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points,
        # INT count, REAL tension);
        GdipDrawCurve2 = gdiplus.GdipDrawCurve2
        GdipDrawCurve2.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawCurve2I(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points,
        # INT count, REAL tension);
        GdipDrawCurve2I = gdiplus.GdipDrawCurve2I
        GdipDrawCurve2I.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawCurve3(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPointF *points,
        # INT count, INT offset, INT numberOfSegments, REAL tension);
        GdipDrawCurve3 = gdiplus.GdipDrawCurve3
        GdipDrawCurve3.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawCurve3I(GpGraphics *graphics, GpPen *pen, GDIPCONST GpPoint *points,
        # INT count, INT offset, INT numberOfSegments, REAL tension);
        GdipDrawCurve3I = gdiplus.GdipDrawCurve3I
        GdipDrawCurve3I.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawClosedCurve(GpGraphics *graphics, GpPen *pen,
        # GDIPCONST GpPointF *points, INT count);
        GdipDrawClosedCurve = gdiplus.GdipDrawClosedCurve
        GdipDrawClosedCurve.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawClosedCurveI(GpGraphics *graphics, GpPen *pen,
        # GDIPCONST GpPoint *points, INT count);
        GdipDrawClosedCurveI = gdiplus.GdipDrawClosedCurveI
        GdipDrawClosedCurveI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawClosedCurve2(GpGraphics *graphics, GpPen *pen,
        # GDIPCONST GpPointF *points, INT count, REAL tension);
        GdipDrawClosedCurve2 = gdiplus.GdipDrawClosedCurve2
        GdipDrawClosedCurve2.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipDrawClosedCurve2I(GpGraphics *graphics, GpPen *pen,
        # GDIPCONST GpPoint *points, INT count, REAL tension);
        GdipDrawClosedCurve2I = gdiplus.GdipDrawClosedCurve2I
        GdipDrawClosedCurve2I.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipGraphicsClear(GpGraphics *graphics, ARGB color);
        GdipGraphicsClear = gdiplus.GdipGraphicsClear
        GdipGraphicsClear.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillRectangle(GpGraphics *graphics, GpBrush *brush, REAL x, REAL y,
        # REAL width, REAL height);
        GdipFillRectangle = gdiplus.GdipFillRectangle
        GdipFillRectangle.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillRectangleI(GpGraphics *graphics, GpBrush *brush, INT x, INT y,
        # INT width, INT height);
        GdipFillRectangleI = gdiplus.GdipFillRectangleI
        GdipFillRectangleI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillRectangles(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpRectF *rects, INT count);
        GdipFillRectangles = gdiplus.GdipFillRectangles
        GdipFillRectangles.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillRectanglesI(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpRect *rects, INT count);
        GdipFillRectanglesI = gdiplus.GdipFillRectanglesI
        GdipFillRectanglesI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillPolygon(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPointF *points, INT count, GpFillMode fillMode);
        GdipFillPolygon = gdiplus.GdipFillPolygon
        GdipFillPolygon.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillPolygonI(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPoint *points, INT count, GpFillMode fillMode);
        GdipFillPolygonI = gdiplus.GdipFillPolygonI
        GdipFillPolygonI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillPolygon2(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPointF *points, INT count);
        GdipFillPolygon2 = gdiplus.GdipFillPolygon2
        GdipFillPolygon2.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillPolygon2I(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPoint *points, INT count);
        GdipFillPolygon2I = gdiplus.GdipFillPolygon2I
        GdipFillPolygon2I.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillEllipse(GpGraphics *graphics, GpBrush *brush, REAL x, REAL y,
        # REAL width, REAL height);
        GdipFillEllipse = gdiplus.GdipFillEllipse
        GdipFillEllipse.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillEllipseI(GpGraphics *graphics, GpBrush *brush, INT x, INT y,
        # INT width, INT height);
        GdipFillEllipseI = gdiplus.GdipFillEllipseI
        GdipFillEllipseI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillPie(GpGraphics *graphics, GpBrush *brush, REAL x, REAL y,
        # REAL width, REAL height, REAL startAngle, REAL sweepAngle);
        GdipFillPie = gdiplus.GdipFillPie
        GdipFillPie.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillPieI(GpGraphics *graphics, GpBrush *brush, INT x, INT y,
        # INT width, INT height, REAL startAngle, REAL sweepAngle);
        GdipFillPieI = gdiplus.GdipFillPieI
        GdipFillPieI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillPath(GpGraphics *graphics, GpBrush *brush, GpPath *path);
        GdipFillPath = gdiplus.GdipFillPath
        GdipFillPath.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillClosedCurve(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPointF *points, INT count);
        GdipFillClosedCurve = gdiplus.GdipFillClosedCurve
        GdipFillClosedCurve.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillClosedCurveI(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPoint *points, INT count);
        GdipFillClosedCurveI = gdiplus.GdipFillClosedCurveI
        GdipFillClosedCurveI.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillClosedCurve2(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPointF *points, INT count,
        # REAL tension, GpFillMode fillMode);
        GdipFillClosedCurve2 = gdiplus.GdipFillClosedCurve2
        GdipFillClosedCurve2.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillClosedCurve2I(GpGraphics *graphics, GpBrush *brush,
        # GDIPCONST GpPoint *points, INT count,
        # REAL tension, GpFillMode fillMode);
        GdipFillClosedCurve2I = gdiplus.GdipFillClosedCurve2I
        GdipFillClosedCurve2I.restype = GpStatus
        # GpStatus WINGDIPAPI
        # GdipFillRegion(GpGraphics *graphics, GpBrush *brush,
        # GpRegion *region);
        GdipFillRegion = gdiplus.GdipFillRegion
        GdipFillRegion.restype = GpStatus
        if GDIPVER >= 0x0110:
            # GpStatus
            # WINGDIPAPI
            # GdipDrawImageFX(
            # GpGraphics *graphics,
            # GpImage *image,
            # GpRectF *source,
            # GpMatrix *xForm,
            # CGpEffect *effect,
            # GpImageAttributes *imageAttributes,
            # GpUnit srcUnit
            # );
            GdipDrawImageFX = gdiplus.GdipDrawImageFX
            GdipDrawImageFX.restype = GpStatus


        # END IF  (GDIPVER >= 0x0110)

        # GpStatus WINGDIPAPI
        # GdipDrawImage(GpGraphics *graphics, GpImage *image, REAL x, REAL y);
        GdipDrawImage = gdiplus.GdipDrawImage
        GdipDrawImage.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImageI(GpGraphics *graphics, GpImage *image, INT x, INT y);
        GdipDrawImageI = gdiplus.GdipDrawImageI
        GdipDrawImageI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImageRect(GpGraphics *graphics, GpImage *image, REAL x, REAL y,
        # REAL width, REAL height);
        GdipDrawImageRect = gdiplus.GdipDrawImageRect
        GdipDrawImageRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImageRectI(GpGraphics *graphics, GpImage *image, INT x, INT y,
        # INT width, INT height);
        GdipDrawImageRectI = gdiplus.GdipDrawImageRectI
        GdipDrawImageRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImagePoints(GpGraphics *graphics, GpImage *image,
        # GDIPCONST GpPointF *dstpoints, INT count);
        GdipDrawImagePoints = gdiplus.GdipDrawImagePoints
        GdipDrawImagePoints.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImagePointsI(GpGraphics *graphics, GpImage *image,
        # GDIPCONST GpPoint *dstpoints, INT count);
        GdipDrawImagePointsI = gdiplus.GdipDrawImagePointsI
        GdipDrawImagePointsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImagePointRect(GpGraphics *graphics, GpImage *image, REAL x,
        # REAL y, REAL srcx, REAL srcy, REAL srcwidth,
        # REAL srcheight, GpUnit srcUnit);
        GdipDrawImagePointRect = gdiplus.GdipDrawImagePointRect
        GdipDrawImagePointRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImagePointRectI(GpGraphics *graphics, GpImage *image, INT x,
        # INT y, INT srcx, INT srcy, INT srcwidth,
        # INT srcheight, GpUnit srcUnit);
        GdipDrawImagePointRectI = gdiplus.GdipDrawImagePointRectI
        GdipDrawImagePointRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImageRectRect(GpGraphics *graphics, GpImage *image, REAL dstx,
        # REAL dsty, REAL dstwidth, REAL dstheight,
        # REAL srcx, REAL srcy, REAL srcwidth, REAL srcheight,
        # GpUnit srcUnit,
        # GDIPCONST GpImageAttributes* imageAttributes,
        # DrawImageAbort callback, VOID * callbackData);
        GdipDrawImageRectRect = gdiplus.GdipDrawImageRectRect
        GdipDrawImageRectRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImageRectRectI(GpGraphics *graphics, GpImage *image, INT dstx,
        # INT dsty, INT dstwidth, INT dstheight,
        # INT srcx, INT srcy, INT srcwidth, INT srcheight,
        # GpUnit srcUnit,
        # GDIPCONST GpImageAttributes* imageAttributes,
        # DrawImageAbort callback, VOID * callbackData);
        GdipDrawImageRectRectI = gdiplus.GdipDrawImageRectRectI
        GdipDrawImageRectRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImagePointsRect(GpGraphics *graphics, GpImage *image,
        # GDIPCONST GpPointF *points, INT count, REAL srcx,
        # REAL srcy, REAL srcwidth, REAL srcheight,
        # GpUnit srcUnit,
        # GDIPCONST GpImageAttributes* imageAttributes,
        # DrawImageAbort callback, VOID * callbackData);
        GdipDrawImagePointsRect = gdiplus.GdipDrawImagePointsRect
        GdipDrawImagePointsRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawImagePointsRectI(GpGraphics *graphics, GpImage *image,
        # GDIPCONST GpPoint *points, INT count, INT srcx,
        # INT srcy, INT srcwidth, INT srcheight,
        # GpUnit srcUnit,
        # GDIPCONST GpImageAttributes* imageAttributes,
        # DrawImageAbort callback, VOID * callbackData);
        GdipDrawImagePointsRectI = gdiplus.GdipDrawImagePointsRectI
        GdipDrawImagePointsRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileDestPoint(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST PointF &      destPoint,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileDestPoint = gdiplus.GdipEnumerateMetafileDestPoint
        GdipEnumerateMetafileDestPoint.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileDestPointI(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST Point &       destPoint,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileDestPointI = (
            gdiplus.GdipEnumerateMetafileDestPointI
        )
        GdipEnumerateMetafileDestPointI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileDestRect(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST RectF &       destRect,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileDestRect = gdiplus.GdipEnumerateMetafileDestRect
        GdipEnumerateMetafileDestRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileDestRectI(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST Rect &        destRect,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileDestRectI = gdiplus.GdipEnumerateMetafileDestRectI
        GdipEnumerateMetafileDestRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileDestPoints(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST PointF *      destPoints,
        # INT                     count,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileDestPoints = (
            gdiplus.GdipEnumerateMetafileDestPoints
        )
        GdipEnumerateMetafileDestPoints.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileDestPointsI(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST Point *       destPoints,
        # INT                     count,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileDestPointsI = (
            gdiplus.GdipEnumerateMetafileDestPointsI
        )
        GdipEnumerateMetafileDestPointsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileSrcRectDestPoint(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST PointF &      destPoint,
        # GDIPCONST RectF &       srcRect,
        # Unit                    srcUnit,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileSrcRectDestPoint = (
            gdiplus.GdipEnumerateMetafileSrcRectDestPoint
        )
        GdipEnumerateMetafileSrcRectDestPoint.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileSrcRectDestPointI(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST Point &       destPoint,
        # GDIPCONST Rect &        srcRect,
        # Unit                    srcUnit,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileSrcRectDestPointI = (
            gdiplus.GdipEnumerateMetafileSrcRectDestPointI
        )
        GdipEnumerateMetafileSrcRectDestPointI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileSrcRectDestRect(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST RectF &       destRect,
        # GDIPCONST RectF &       srcRect,
        # Unit                    srcUnit,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileSrcRectDestRect = (
            gdiplus.GdipEnumerateMetafileSrcRectDestRect
        )
        GdipEnumerateMetafileSrcRectDestRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileSrcRectDestRectI(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST Rect &        destRect,
        # GDIPCONST Rect &        srcRect,
        # Unit                    srcUnit,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileSrcRectDestRectI = (
            gdiplus.GdipEnumerateMetafileSrcRectDestRectI
        )
        GdipEnumerateMetafileSrcRectDestRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileSrcRectDestPoints(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST PointF *      destPoints,
        # INT                     count,
        # GDIPCONST RectF &       srcRect,
        # Unit                    srcUnit,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileSrcRectDestPoints = (
            gdiplus.GdipEnumerateMetafileSrcRectDestPoints
        )
        GdipEnumerateMetafileSrcRectDestPoints.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEnumerateMetafileSrcRectDestPointsI(
        # GpGraphics *            graphics,
        # GDIPCONST GpMetafile *  metafile,
        # GDIPCONST Point *       destPoints,
        # INT                     count,
        # GDIPCONST Rect &        srcRect,
        # Unit                    srcUnit,
        # EnumerateMetafileProc   callback,
        # VOID *                  callbackData,
        # GDIPCONST GpImageAttributes *     imageAttributes
        # );
        GdipEnumerateMetafileSrcRectDestPointsI = (
            gdiplus.GdipEnumerateMetafileSrcRectDestPointsI
        )
        GdipEnumerateMetafileSrcRectDestPointsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipPlayMetafileRecord(
        # GDIPCONST GpMetafile *  metafile,
        # EmfPlusRecordType       recordType,
        # UINT                    flags,
        # UINT                    dataSize,
        # GDIPCONST BYTE *        data
        # );
        GdipPlayMetafileRecord = gdiplus.GdipPlayMetafileRecord
        GdipPlayMetafileRecord.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetClipGraphics(GpGraphics *graphics, GpGraphics *srcgraphics,
        # CombineMode combineMode);
        GdipSetClipGraphics = gdiplus.GdipSetClipGraphics
        GdipSetClipGraphics.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetClipRect(GpGraphics *graphics, REAL x, REAL y,
        # REAL width, REAL height, CombineMode combineMode);
        GdipSetClipRect = gdiplus.GdipSetClipRect
        GdipSetClipRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetClipRectI(GpGraphics *graphics, INT x, INT y,
        # INT width, INT height, CombineMode combineMode);
        GdipSetClipRectI = gdiplus.GdipSetClipRectI
        GdipSetClipRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetClipPath(GpGraphics *graphics, GpPath *path, CombineMode combineMode);
        GdipSetClipPath = gdiplus.GdipSetClipPath
        GdipSetClipPath.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetClipRegion(GpGraphics *graphics, GpRegion *region,
        # CombineMode combineMode);
        GdipSetClipRegion = gdiplus.GdipSetClipRegion
        GdipSetClipRegion.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetClipHrgn(GpGraphics *graphics, HRGN hRgn, CombineMode combineMode);
        GdipSetClipHrgn = gdiplus.GdipSetClipHrgn
        GdipSetClipHrgn.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipResetClip(GpGraphics *graphics);
        GdipResetClip = gdiplus.GdipResetClip
        GdipResetClip.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTranslateClip(GpGraphics *graphics, REAL dx, REAL dy);
        GdipTranslateClip = gdiplus.GdipTranslateClip
        GdipTranslateClip.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTranslateClipI(GpGraphics *graphics, INT dx, INT dy);
        GdipTranslateClipI = gdiplus.GdipTranslateClipI
        GdipTranslateClipI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetClip(GpGraphics *graphics, GpRegion *region);
        GdipGetClip = gdiplus.GdipGetClip
        GdipGetClip.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetClipBounds(GpGraphics *graphics, GpRectF *rect);
        GdipGetClipBounds = gdiplus.GdipGetClipBounds
        GdipGetClipBounds.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetClipBoundsI(GpGraphics *graphics, GpRect *rect);
        GdipGetClipBoundsI = gdiplus.GdipGetClipBoundsI
        GdipGetClipBoundsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsClipEmpty(GpGraphics *graphics, BOOL *result);
        GdipIsClipEmpty = gdiplus.GdipIsClipEmpty
        GdipIsClipEmpty.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetVisibleClipBounds(GpGraphics *graphics, GpRectF *rect);
        GdipGetVisibleClipBounds = gdiplus.GdipGetVisibleClipBounds
        GdipGetVisibleClipBounds.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetVisibleClipBoundsI(GpGraphics *graphics, GpRect *rect);
        GdipGetVisibleClipBoundsI = gdiplus.GdipGetVisibleClipBoundsI
        GdipGetVisibleClipBoundsI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisibleClipEmpty(GpGraphics *graphics, BOOL *result);
        GdipIsVisibleClipEmpty = gdiplus.GdipIsVisibleClipEmpty
        GdipIsVisibleClipEmpty.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisiblePoint(GpGraphics *graphics, REAL x, REAL y,
        # BOOL *result);
        GdipIsVisiblePoint = gdiplus.GdipIsVisiblePoint
        GdipIsVisiblePoint.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisiblePointI(GpGraphics *graphics, INT x, INT y,
        # BOOL *result);
        GdipIsVisiblePointI = gdiplus.GdipIsVisiblePointI
        GdipIsVisiblePointI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisibleRect(GpGraphics *graphics, REAL x, REAL y,
        # REAL width, REAL height, BOOL *result);
        GdipIsVisibleRect = gdiplus.GdipIsVisibleRect
        GdipIsVisibleRect.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipIsVisibleRectI(GpGraphics *graphics, INT x, INT y,
        # INT width, INT height, BOOL *result);
        GdipIsVisibleRectI = gdiplus.GdipIsVisibleRectI
        GdipIsVisibleRectI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSaveGraphics(GpGraphics *graphics, GraphicsState *state);
        GdipSaveGraphics = gdiplus.GdipSaveGraphics
        GdipSaveGraphics.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRestoreGraphics(GpGraphics *graphics, GraphicsState state);
        GdipRestoreGraphics = gdiplus.GdipRestoreGraphics
        GdipRestoreGraphics.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipBeginContainer(GpGraphics *graphics, GDIPCONST GpRectF* dstrect,
        # GDIPCONST GpRectF *srcrect, GpUnit unit,
        # GraphicsContainer *state);
        GdipBeginContainer = gdiplus.GdipBeginContainer
        GdipBeginContainer.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipBeginContainerI(GpGraphics *graphics, GDIPCONST GpRect* dstrect,
        # GDIPCONST GpRect *srcrect, GpUnit unit,
        # GraphicsContainer *state);
        GdipBeginContainerI = gdiplus.GdipBeginContainerI
        GdipBeginContainerI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipBeginContainer2(GpGraphics *graphics, GraphicsContainer* state);
        GdipBeginContainer2 = gdiplus.GdipBeginContainer2
        GdipBeginContainer2.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipEndContainer(GpGraphics *graphics, GraphicsContainer state);
        GdipEndContainer = gdiplus.GdipEndContainer
        GdipEndContainer.restype = GpStatus


        # GpStatus
        # GdipGetMetafileHeaderFromWmf(
        # HMETAFILE           hWmf,
        # GDIPCONST WmfPlaceableFileHeader *     wmfPlaceableFileHeader,
        # MetafileHeader *    header
        # );
        GdipGetMetafileHeaderFromWmf = gdiplus.GdipGetMetafileHeaderFromWmf
        GdipGetMetafileHeaderFromWmf.restype = GpStatus


        # GpStatus
        # WINGDIPAPI
        # GdipGetMetafileHeaderFromEmf(
        # HENHMETAFILE        hEmf,
        # MetafileHeader *    header
        # );
        GdipGetMetafileHeaderFromEmf = gdiplus.GdipGetMetafileHeaderFromEmf
        GdipGetMetafileHeaderFromEmf.restype = GpStatus


        # GpStatus
        # WINGDIPAPI
        # GdipGetMetafileHeaderFromFile(
        # GDIPCONST WCHAR*        filename,
        # MetafileHeader *    header
        # );
        GdipGetMetafileHeaderFromFile = gdiplus.GdipGetMetafileHeaderFromFile
        GdipGetMetafileHeaderFromFile.restype = GpStatus


        # GpStatus
        # WINGDIPAPI
        # GdipGetMetafileHeaderFromStream(
        # IStream *           stream,
        # MetafileHeader *    header
        # );
        GdipGetMetafileHeaderFromStream = (
            gdiplus.GdipGetMetafileHeaderFromStream
        )
        GdipGetMetafileHeaderFromStream.restype = GpStatus


        # GpStatus
        # WINGDIPAPI
        # GdipGetMetafileHeaderFromMetafile(
        # GpMetafile *        metafile,
        # MetafileHeader *    header
        # );
        GdipGetMetafileHeaderFromMetafile = (
            gdiplus.GdipGetMetafileHeaderFromMetafile
        )
        GdipGetMetafileHeaderFromMetafile.restype = GpStatus


        # GpStatus
        # WINGDIPAPI
        # GdipGetHemfFromMetafile(
        # GpMetafile *        metafile,
        # HENHMETAFILE *      hEmf
        # );
        GdipGetHemfFromMetafile = gdiplus.GdipGetHemfFromMetafile
        GdipGetHemfFromMetafile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateStreamOnFile(GDIPCONST WCHAR * filename, UINT access,
        # IStream **stream);
        GdipCreateStreamOnFile = gdiplus.GdipCreateStreamOnFile
        GdipCreateStreamOnFile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMetafileFromWmf(HMETAFILE hWmf, BOOL deleteWmf,
        # GDIPCONST WmfPlaceableFileHeader * wmfPlaceableFileHeader,
        # GpMetafile **metafile);
        GdipCreateMetafileFromWmf = gdiplus.GdipCreateMetafileFromWmf
        GdipCreateMetafileFromWmf.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMetafileFromEmf(HENHMETAFILE hEmf, BOOL deleteEmf,
        # GpMetafile **metafile);
        GdipCreateMetafileFromEmf = gdiplus.GdipCreateMetafileFromEmf
        GdipCreateMetafileFromEmf.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMetafileFromFile(GDIPCONST WCHAR* file, GpMetafile **metafile);
        GdipCreateMetafileFromFile = gdiplus.GdipCreateMetafileFromFile
        GdipCreateMetafileFromFile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMetafileFromWmfFile(GDIPCONST WCHAR* file,
        # GDIPCONST WmfPlaceableFileHeader * wmfPlaceableFileHeader,
        # GpMetafile **metafile);
        GdipCreateMetafileFromWmfFile = gdiplus.GdipCreateMetafileFromWmfFile
        GdipCreateMetafileFromWmfFile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateMetafileFromStream(IStream * stream, GpMetafile **metafile);
        GdipCreateMetafileFromStream = gdiplus.GdipCreateMetafileFromStream
        GdipCreateMetafileFromStream.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRecordMetafile(
        # HDC                 referenceHdc,
        # EmfType             type,
        # GDIPCONST GpRectF * frameRect,
        # MetafileFrameUnit   frameUnit,
        # GDIPCONST WCHAR *   description,
        # GpMetafile **       metafile
        # );
        GdipRecordMetafile = gdiplus.GdipRecordMetafile
        GdipRecordMetafile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRecordMetafileI(
        # HDC                 referenceHdc,
        # EmfType             type,
        # GDIPCONST GpRect *  frameRect,
        # MetafileFrameUnit   frameUnit,
        # GDIPCONST WCHAR *   description,
        # GpMetafile **       metafile
        # );
        GdipRecordMetafileI = gdiplus.GdipRecordMetafileI
        GdipRecordMetafileI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRecordMetafileFileName(
        # GDIPCONST WCHAR*    fileName,
        # HDC                 referenceHdc,
        # EmfType             type,
        # GDIPCONST GpRectF * frameRect,
        # MetafileFrameUnit   frameUnit,
        # GDIPCONST WCHAR *   description,
        # GpMetafile **       metafile
        # );
        GdipRecordMetafileFileName = gdiplus.GdipRecordMetafileFileName
        GdipRecordMetafileFileName.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRecordMetafileFileNameI(
        # GDIPCONST WCHAR*    fileName,
        # HDC                 referenceHdc,
        # EmfType             type,
        # GDIPCONST GpRect *  frameRect,
        # MetafileFrameUnit   frameUnit,
        # GDIPCONST WCHAR *   description,
        # GpMetafile **       metafile
        # );
        GdipRecordMetafileFileNameI = gdiplus.GdipRecordMetafileFileNameI
        GdipRecordMetafileFileNameI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRecordMetafileStream(
        # IStream *           stream,
        # HDC                 referenceHdc,
        # EmfType             type,
        # GDIPCONST GpRectF * frameRect,
        # MetafileFrameUnit   frameUnit,
        # GDIPCONST WCHAR *   description,
        # GpMetafile **       metafile
        # );
        GdipRecordMetafileStream = gdiplus.GdipRecordMetafileStream
        GdipRecordMetafileStream.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipRecordMetafileStreamI(
        # IStream *           stream,
        # HDC                 referenceHdc,
        # EmfType             type,
        # GDIPCONST GpRect *  frameRect,
        # MetafileFrameUnit   frameUnit,
        # GDIPCONST WCHAR *   description,
        # GpMetafile **       metafile
        # );
        GdipRecordMetafileStreamI = gdiplus.GdipRecordMetafileStreamI
        GdipRecordMetafileStreamI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetMetafileDownLevelRasterizationLimit(
        # GpMetafile *            metafile,
        # UINT                    metafileRasterizationLimitDpi
        # );
        GdipSetMetafileDownLevelRasterizationLimit = (
            gdiplus.GdipSetMetafileDownLevelRasterizationLimit
        )
        GdipSetMetafileDownLevelRasterizationLimit.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetMetafileDownLevelRasterizationLimit(
        # GDIPCONST GpMetafile *  metafile,
        # UINT *                  metafileRasterizationLimitDpi
        # );
        GdipGetMetafileDownLevelRasterizationLimit = (
            gdiplus.GdipGetMetafileDownLevelRasterizationLimit
        )
        GdipGetMetafileDownLevelRasterizationLimit.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageDecoders(_In_ UINT numDecoders,
        # _In_ UINT size,
        # _Out_writes_bytes_(size) ImageCodecInfo *decoders);
        GdipGetImageDecoders = gdiplus.GdipGetImageDecoders
        GdipGetImageDecoders.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetImageEncoders(_In_ UINT numEncoders,
        # _In_ UINT size,
        # _Out_writes_bytes_(size) ImageCodecInfo *encoders);
        GdipGetImageEncoders = gdiplus.GdipGetImageEncoders
        GdipGetImageEncoders.restype = GpStatus

        # ------------------------------------------------------------------
        # FontFamily APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateFontFamilyFromName(GDIPCONST WCHAR *name,
        # GpFontCollection *fontCollection,
        # GpFontFamily **fontFamily);
        GdipCreateFontFamilyFromName = gdiplus.GdipCreateFontFamilyFromName
        GdipCreateFontFamilyFromName.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeleteFontFamily(GpFontFamily *fontFamily);
        GdipDeleteFontFamily = gdiplus.GdipDeleteFontFamily
        GdipDeleteFontFamily.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCloneFontFamily(GpFontFamily *fontFamily, GpFontFamily **clonedFontFamily);
        GdipCloneFontFamily = gdiplus.GdipCloneFontFamily
        GdipCloneFontFamily.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetGenericFontFamilySansSerif(GpFontFamily **nativeFamily);
        GdipGetGenericFontFamilySansSerif = (
            gdiplus.GdipGetGenericFontFamilySansSerif
        )
        GdipGetGenericFontFamilySansSerif.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetGenericFontFamilySerif(GpFontFamily **nativeFamily);
        GdipGetGenericFontFamilySerif = gdiplus.GdipGetGenericFontFamilySerif
        GdipGetGenericFontFamilySerif.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetGenericFontFamilyMonospace(GpFontFamily **nativeFamily);
        GdipGetGenericFontFamilyMonospace = (
            gdiplus.GdipGetGenericFontFamilyMonospace
        )
        GdipGetGenericFontFamilyMonospace.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFamilyName(
        # GDIPCONST GpFontFamily              *family,
        # _Out_writes_(LF_FACESIZE) LPWSTR    name,
        # LANGID                              language
        # );
        GdipGetFamilyName = gdiplus.GdipGetFamilyName
        GdipGetFamilyName.restype = GpStatus


        # GpStatus   WINGDIPAPI
        # GdipIsStyleAvailable(GDIPCONST GpFontFamily *family, INT style,
        # BOOL * IsStyleAvailable);
        GdipIsStyleAvailable = gdiplus.GdipIsStyleAvailable
        GdipIsStyleAvailable.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipFontCollectionEnumerable(
        # GpFontCollection* fontCollection,
        # GpGraphics* graphics,
        # INT *       numFound
        # );
        GdipFontCollectionEnumerable = gdiplus.GdipFontCollectionEnumerable
        GdipFontCollectionEnumerable.restype = GpStatus

        # GpStatus WINGDIPAPI GdipFontCollectionEnumerate(
        # GpFontCollection* fontCollection,
        # INT             numSought,
        # GpFontFamily*   gpfamilies[],
        # INT*            numFound,
        # GpGraphics*     graphics
        # );
        GdipFontCollectionEnumerate = gdiplus.GdipFontCollectionEnumerate
        GdipFontCollectionEnumerate.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetEmHeight(GDIPCONST GpFontFamily *family, INT style,
        # UINT16 * EmHeight);
        GdipGetEmHeight = gdiplus.GdipGetEmHeight
        GdipGetEmHeight.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetCellAscent(GDIPCONST GpFontFamily *family, INT style,
        # UINT16 * CellAscent);
        GdipGetCellAscent = gdiplus.GdipGetCellAscent
        GdipGetCellAscent.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetCellDescent(GDIPCONST GpFontFamily *family, INT style,
        # UINT16 * CellDescent);
        GdipGetCellDescent = gdiplus.GdipGetCellDescent
        GdipGetCellDescent.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLineSpacing(GDIPCONST GpFontFamily *family, INT style,
        # UINT16 * LineSpacing);
        GdipGetLineSpacing = gdiplus.GdipGetLineSpacing
        GdipGetLineSpacing.restype = GpStatus

        # ------------------------------------------------------------------
        # Font APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateFontFromDC(
        # HDC        hdc,
        # GpFont   **font
        # );
        GdipCreateFontFromDC = gdiplus.GdipCreateFontFromDC
        GdipCreateFontFromDC.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateFontFromLogfontA(
        # HDC        hdc,
        # GDIPCONST LOGFONTA  *logfont,
        # GpFont   **font
        # );
        GdipCreateFontFromLogfontA = gdiplus.GdipCreateFontFromLogfontA
        GdipCreateFontFromLogfontA.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateFontFromLogfontW(
        # HDC        hdc,
        # GDIPCONST LOGFONTW  *logfont,
        # GpFont   **font
        # );
        GdipCreateFontFromLogfontW = gdiplus.GdipCreateFontFromLogfontW
        GdipCreateFontFromLogfontW.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCreateFont(
        # GDIPCONST GpFontFamily  *fontFamily,
        # REAL                 emSize,
        # INT                  style,
        # Unit                 unit,
        # GpFont             **font
        # );
        GdipCreateFont = gdiplus.GdipCreateFont
        GdipCreateFont.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFamily(GpFont *font, GpFontFamily **family);
        GdipGetFamily = gdiplus.GdipGetFamily
        GdipGetFamily.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFontStyle(GpFont *font, INT *style);
        GdipGetFontStyle = gdiplus.GdipGetFontStyle
        GdipGetFontStyle.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFontSize(GpFont *font, REAL *size);
        GdipGetFontSize = gdiplus.GdipGetFontSize
        GdipGetFontSize.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFontUnit(GpFont *font, Unit *unit);
        GdipGetFontUnit = gdiplus.GdipGetFontUnit
        GdipGetFontUnit.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFontHeight(GDIPCONST GpFont *font, GDIPCONST GpGraphics *graphics,
        # REAL *height);
        GdipGetFontHeight = gdiplus.GdipGetFontHeight
        GdipGetFontHeight.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFontHeightGivenDPI(GDIPCONST GpFont *font, REAL dpi, REAL *height);
        GdipGetFontHeightGivenDPI = gdiplus.GdipGetFontHeightGivenDPI
        GdipGetFontHeightGivenDPI.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLogFontA(GpFont * font, GpGraphics *graphics, LOGFONTA * logfontA);
        GdipGetLogFontA = gdiplus.GdipGetLogFontA
        GdipGetLogFontA.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetLogFontW(GpFont * font, GpGraphics *graphics, LOGFONTW * logfontW);
        GdipGetLogFontW = gdiplus.GdipGetLogFontW
        GdipGetLogFontW.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetFontCollectionFamilyCount(
        # GpFontCollection* fontCollection,
        # INT *       numFound
        # );
        GdipGetFontCollectionFamilyCount = (
            gdiplus.GdipGetFontCollectionFamilyCount
        )
        GdipGetFontCollectionFamilyCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipPrivateAddFontFile(
        # GpFontCollection* fontCollection,
        # GDIPCONST WCHAR* filename
        # );
        GdipPrivateAddFontFile = gdiplus.GdipPrivateAddFontFile
        GdipPrivateAddFontFile.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipPrivateAddMemoryFont(
        # GpFontCollection* fontCollection,
        # GDIPCONST void* memory,
        # INT length
        # );
        GdipPrivateAddMemoryFont = gdiplus.GdipPrivateAddMemoryFont
        GdipPrivateAddMemoryFont.restype = GpStatus

        # ------------------------------------------------------------------
        # Text APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipDrawString(
        # GpGraphics               *graphics,
        # GDIPCONST WCHAR          *string,
        # INT                       length,
        # GDIPCONST GpFont         *font,
        # GDIPCONST RectF          *layoutRect,
        # GDIPCONST GpStringFormat *stringFormat,
        # GDIPCONST GpBrush        *brush
        # );
        GdipDrawString = gdiplus.GdipDrawString
        GdipDrawString.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipMeasureString(
        # GpGraphics               *graphics,
        # GDIPCONST WCHAR          *string,
        # INT                       length,
        # GDIPCONST GpFont         *font,
        # GDIPCONST RectF          *layoutRect,
        # GDIPCONST GpStringFormat *stringFormat,
        # RectF                    *boundingBox,
        # INT                      *codepointsFitted,
        # INT                      *linesFilled
        # );
        GdipMeasureString = gdiplus.GdipMeasureString
        GdipMeasureString.restype = GpStatus

        # GpStatus
        # WINGDIPAPI
        # GdipMeasureCharacterRanges(
        # GpGraphics               *graphics,
        # GDIPCONST WCHAR          *string,
        # INT                       length,
        # GDIPCONST GpFont         *font,
        # GDIPCONST RectF           & layoutRect,
        # GDIPCONST GpStringFormat *stringFormat,
        # INT                       regionCount,
        # GpRegion                **regions
        # );
        GdipMeasureCharacterRanges = gdiplus.GdipMeasureCharacterRanges
        GdipMeasureCharacterRanges.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawDriverString(
        # GpGraphics *graphics,
        # GDIPCONST UINT16 *text,
        # INT length,
        # GDIPCONST GpFont *font,
        # GDIPCONST GpBrush *brush,
        # GDIPCONST PointF *positions,
        # INT flags,
        # GDIPCONST GpMatrix *matrix
        # );
        GdipDrawDriverString = gdiplus.GdipDrawDriverString
        GdipDrawDriverString.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipMeasureDriverString(
        # GpGraphics *graphics,
        # GDIPCONST UINT16 *text,
        # INT length,
        # GDIPCONST GpFont *font,
        # GDIPCONST PointF *positions,
        # INT flags,
        # GDIPCONST GpMatrix *matrix,
        # RectF *boundingBox
        # );
        GdipMeasureDriverString = gdiplus.GdipMeasureDriverString
        GdipMeasureDriverString.restype = GpStatus

        # ------------------------------------------------------------------
        # String format APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateStringFormat(
        # INT               formatAttributes,
        # LANGID            language,
        # GpStringFormat  **format
        # );
        GdipCreateStringFormat = gdiplus.GdipCreateStringFormat
        GdipCreateStringFormat.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipStringFormatGetGenericDefault(GpStringFormat **format);
        GdipStringFormatGetGenericDefault = (
            gdiplus.GdipStringFormatGetGenericDefault
        )
        GdipStringFormatGetGenericDefault.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipStringFormatGetGenericTypographic(GpStringFormat **format);
        GdipStringFormatGetGenericTypographic = (
            gdiplus.GdipStringFormatGetGenericTypographic
        )
        GdipStringFormatGetGenericTypographic.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeleteStringFormat(GpStringFormat *format);
        GdipDeleteStringFormat = gdiplus.GdipDeleteStringFormat
        GdipDeleteStringFormat.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipCloneStringFormat(GDIPCONST GpStringFormat *format,
        # GpStringFormat **newFormat);
        GdipCloneStringFormat = gdiplus.GdipCloneStringFormat
        GdipCloneStringFormat.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatFlags(GpStringFormat *format, INT flags);
        GdipSetStringFormatFlags = gdiplus.GdipSetStringFormatFlags
        GdipSetStringFormatFlags.restype = GpStatus

        # GpStatus WINGDIPAPI GdipGetStringFormatFlags(GDIPCONST GpStringFormat *format,
        # INT *flags);
        GdipGetStringFormatFlags = gdiplus.GdipGetStringFormatFlags
        GdipGetStringFormatFlags.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatAlign(GpStringFormat *format, StringAlignment align);
        GdipSetStringFormatAlign = gdiplus.GdipSetStringFormatAlign
        GdipSetStringFormatAlign.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatAlign(GDIPCONST GpStringFormat *format,
        # StringAlignment *align);
        GdipGetStringFormatAlign = gdiplus.GdipGetStringFormatAlign
        GdipGetStringFormatAlign.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatLineAlign(GpStringFormat *format,
        # StringAlignment align);
        GdipSetStringFormatLineAlign = gdiplus.GdipSetStringFormatLineAlign
        GdipSetStringFormatLineAlign.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatLineAlign(GDIPCONST GpStringFormat *format,
        # StringAlignment *align);
        GdipGetStringFormatLineAlign = gdiplus.GdipGetStringFormatLineAlign
        GdipGetStringFormatLineAlign.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatTrimming(
        # GpStringFormat  *format,
        # StringTrimming   trimming
        # );
        GdipSetStringFormatTrimming = gdiplus.GdipSetStringFormatTrimming
        GdipSetStringFormatTrimming.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatTrimming(
        # GDIPCONST GpStringFormat *format,
        # StringTrimming       *trimming
        # );
        GdipGetStringFormatTrimming = gdiplus.GdipGetStringFormatTrimming
        GdipGetStringFormatTrimming.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatHotkeyPrefix(GpStringFormat *format, INT hotkeyPrefix);
        GdipSetStringFormatHotkeyPrefix = (
            gdiplus.GdipSetStringFormatHotkeyPrefix
        )
        GdipSetStringFormatHotkeyPrefix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatHotkeyPrefix(GDIPCONST GpStringFormat *format,
        # INT *hotkeyPrefix);
        GdipGetStringFormatHotkeyPrefix = (
            gdiplus.GdipGetStringFormatHotkeyPrefix
        )
        GdipGetStringFormatHotkeyPrefix.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatTabStops(GpStringFormat *format, REAL firstTabOffset,
        # INT count, GDIPCONST REAL *tabStops);
        GdipSetStringFormatTabStops = gdiplus.GdipSetStringFormatTabStops
        GdipSetStringFormatTabStops.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatTabStops(GDIPCONST GpStringFormat *format, INT count,
        # REAL *firstTabOffset, REAL *tabStops);
        GdipGetStringFormatTabStops = gdiplus.GdipGetStringFormatTabStops
        GdipGetStringFormatTabStops.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatTabStopCount(GDIPCONST GpStringFormat *format, INT * count);
        GdipGetStringFormatTabStopCount = (
            gdiplus.GdipGetStringFormatTabStopCount
        )
        GdipGetStringFormatTabStopCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatDigitSubstitution(GpStringFormat *format, LANGID language,
        # StringDigitSubstitute substitute);
        GdipSetStringFormatDigitSubstitution = (
            gdiplus.GdipSetStringFormatDigitSubstitution
        )
        GdipSetStringFormatDigitSubstitution.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatDigitSubstitution(GDIPCONST GpStringFormat *format,
        # LANGID *language,
        # StringDigitSubstitute *substitute);
        GdipGetStringFormatDigitSubstitution = (
            gdiplus.GdipGetStringFormatDigitSubstitution
        )
        GdipGetStringFormatDigitSubstitution.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipGetStringFormatMeasurableCharacterRangeCount(
        # GDIPCONST GpStringFormat    *format,
        # INT                         *count
        # );
        GdipGetStringFormatMeasurableCharacterRangeCount = (
            gdiplus.GdipGetStringFormatMeasurableCharacterRangeCount
        )
        GdipGetStringFormatMeasurableCharacterRangeCount.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetStringFormatMeasurableCharacterRanges(
        # GpStringFormat              *format,
        # INT                         rangeCount,
        # GDIPCONST CharacterRange    *ranges
        # );
        GdipSetStringFormatMeasurableCharacterRanges = (
            gdiplus.GdipSetStringFormatMeasurableCharacterRanges
        )
        GdipSetStringFormatMeasurableCharacterRanges.restype = GpStatus

        # ------------------------------------------------------------------
        # Cached Bitmap APIs
        # ------------------------------------------------------------------
        # GpStatus WINGDIPAPI
        # GdipCreateCachedBitmap(
        # GpBitmap *bitmap,
        # GpGraphics *graphics,
        # GpCachedBitmap **cachedBitmap
        # );
        GdipCreateCachedBitmap = gdiplus.GdipCreateCachedBitmap
        GdipCreateCachedBitmap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDeleteCachedBitmap(GpCachedBitmap *cachedBitmap);
        GdipDeleteCachedBitmap = gdiplus.GdipDeleteCachedBitmap
        GdipDeleteCachedBitmap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipDrawCachedBitmap(
        # GpGraphics *graphics,
        # GpCachedBitmap *cachedBitmap,
        # INT x,
        # INT y
        # );
        GdipDrawCachedBitmap = gdiplus.GdipDrawCachedBitmap
        GdipDrawCachedBitmap.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipSetImageAttributesCachedBackground(
        # GpImageAttributes *imageattr,
        # BOOL enableFlag
        # );
        GdipSetImageAttributesCachedBackground = (
            gdiplus.GdipSetImageAttributesCachedBackground
        )
        GdipSetImageAttributesCachedBackground.restype = GpStatus

        # GpStatus WINGDIPAPI
        # GdipTestControl(
        # GpTestControlEnum control,
        # VOID * param
        # );
        GdipTestControl = gdiplus.GdipTestControl
        GdipTestControl.restype = GpStatus

        # GpStatus WINAPI
        # GdiplusNotificationHook(
        # OUT ULONG_PTR *token
        # );
        GdiplusNotificationHook = gdiplus.GdiplusNotificationHook
        GdiplusNotificationHook.restype = GpStatus

        # VOID WINAPI
        # GdiplusNotificationUnhook(
        # ULONG_PTR token
        # );
        GdiplusNotificationUnhook = gdiplus.GdiplusNotificationUnhook
        GdiplusNotificationUnhook.restype = GpStatus

        if GDIPVER >= 0x0110:
            # GpStatus WINGDIPAPI
            # GdipConvertToEmfPlus(
            # GpGraphics* refGraphics,
            # GpMetafile*  metafile,
            # INT* conversionFailureFlag,
            # EmfType      emfType,
            # WCHAR* description,
            # GpMetafile** out_metafile
            # );
            GdipConvertToEmfPlus = gdiplus.GdipConvertToEmfPlus
            GdipConvertToEmfPlus.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipConvertToEmfPlusToFile(
            # GpGraphics* refGraphics,
            # GpMetafile*  metafile,
            # INT* conversionFailureFlag,
            # WCHAR* filename,
            # EmfType      emfType,
            # WCHAR* description,
            # GpMetafile** out_metafile
            # );
            GdipConvertToEmfPlusToFile = gdiplus.GdipConvertToEmfPlusToFile
            GdipConvertToEmfPlusToFile.restype = GpStatus

            # GpStatus WINGDIPAPI
            # GdipConvertToEmfPlusToStream(
            # GpGraphics* refGraphics,
            # GpMetafile*  metafile,
            # INT* conversionFailureFlag,
            # IStream* stream,
            # EmfType      emfType,
            # WCHAR* description,
            # GpMetafile** out_metafile
            # );
            GdipConvertToEmfPlusToStream = gdiplus.GdipConvertToEmfPlusToStream
            GdipConvertToEmfPlusToStream.restype = GpStatus

        # END IF  (GDIPVER >= 0x0110)

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   not _FLATAPI_H


