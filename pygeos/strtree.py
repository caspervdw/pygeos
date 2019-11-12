from pygeos import lib
import numpy as np

__all__ = ["STRtree"]


class STRtree:
    """A query-only R-tree created using the Sort-Tile-Recursive (STR)
    algorithm.

    For two-dimensional spatial data. The actual tree will be constructed at the first
    query.

    Parameters
    ----------
    geometries : array_like
    leafsize : int
        the maximum number of child nodes that a node can have

    Examples
    --------
    >>> import pygeos
    >>> geoms = pygeos.points(np.arange(10), np.arange(10))
    >>> tree = pygeos.STRtree(geoms)
    >>> tree.query(pygeos.box(2, 2, 4, 4)).tolist()
    [2, 3, 4]
    """

    def __init__(self, geometries, leafsize=5):
        self._tree = lib.STRtree(np.asarray(geometries, dtype=np.object), leafsize)

    def query(self, envelope):
        """Return all items whose extent intersect the given envelope.

        Parameters
        ----------
        envelope : Geometry
        """
        return self._tree.query(envelope)

    @property
    def geometries(self):
        return self._tree.geometries