"""
<file_name>.py
--------------

Graph reconstruction algorithm based on <link to paper, or website, or repository>.

author: <your name here>
email: <name at server dot com> (optional)
Submitted as part of the 2019 NetSI Collabathon.
"""

from .base import BaseReconstructor

class <AlgorithmName>(BaseReconstructor):
    def fit(self, TS):
        """A brief one-line description of the algorithm goes here.

        A short paragraph may follow. The paragraph may include $latex$ by
        enclosing it in dollar signs $\textbf{like this}$.

        Params
        ------
        TS (np.ndarray): Array consisting of $L$ observations from $N$ sensors.

        Returns
        -------
        G (nx.Graph): A reconstructed graph with $N$ nodes.

        """

        # Your code goes here!
        # Your code goes here!
        # Your code goes here!

        # Make sure to always save the final graph object inside the
        # self.results dict as follows:
        self.results['graph'] = G

        # If there are other important quantities that may be of value to
        # the user, you can (and should) also store them in the
        # self.results dict. For example, if the algorithm creates edges by
        # thresholding a matrix of weights, it might be sensible to store
        # this matrix:
        # self.results['matrix'] = unthresholded_matrix

        # The last line MUST be the following. Please make sure that you are only
        # returning the networkx graph object. All other values that may be of
        # importance should be stored in self.results intead.
        return G


### Auxiliary functions go here!
### Auxiliary functions go here!
### Auxiliary functions go here!

# def auxiliary_function1(param1, param2):
#     """Brief description.
#
#     Params
#     ------
#
#     param1 (type): description.
#
#     param2 (type): description.
#
#     Returns
#     -------
#
#     some_value (type) with description.
#
#     """
#     pass

