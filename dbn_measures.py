#  These routines compute distribution measures for discrete distributions.  
#  The input distributions (histograms) do not have to be normalized such 
#  that their values sum to one, but they do have to provide values at the
#  same locations (centers of histogram bins) and, thus, over the same set
#  of locations (they must have the same number of bins).

def OVL_coeff(ct_db1, ct_db2):
#    Compute the Overlapping Coefficient as defined by, for instance: 
#      1. Inman, H. F., and E. L. Bradley Jr., 1989: The Overlapping Coeficient
#         as a Measure of Agreement between Probability Distributions and Point
#         Estimation of the Overlap of Two Normal Densities. Comms. in Stats.-
#         Theory and Methods, 18, 3851-3872.
#      2. Jose, S., S. Thomas, and T. Mathew, 2019: Interval Estimation of the 
#         Overlapping Coefficient of Two Exponential Distributions. J. 
#         Statistical Theory and Appl., 18(1), 26-32.

#    Check if the number of bins in the two distributions are equal.
   check_num_bins(ct_db1, ct_db2)

#    Check for normalization and normalize if needed.    
   (ct_db1, ct_db2) = normalize_dbns(ct_db1, ct_db2)

#    Compute the overlapping coefficient.
   OVLC_val = 0.0
   for i in range(0, len(ct_db1)):
      min_val = min(ct_db1[i], ct_db2[i])
      OVLC_val += min_val

   return OVLC_val

####

def Bhatt_coeff(ct_db1, ct_db2):
#    Compute the Bhattacharyya Coefficient as defined by, for instance: 
#      1. Bhattacharyya, A., On a Measure of Divergence Between two
#         Multinomial Populations. The Indian Journal of Statistics (Sankhya),
#         7(4), 401-406.
#      2. https://en.wikipedia.org/wiki/Bhattacharyya_distance#:~:text=The%20Bhattacharyya%20coefficient%20quantifies%20the,the%20sample%20Bhattacharyya%20coefficient%20is

   import numpy as np

#    Check if the number of bins in the two distributions are equal.
   check_num_bins(ct_db1, ct_db2)

#    Check for normalization and normalize if needed.    
   (ct_db1, ct_db2) = normalize_dbns(ct_db1, ct_db2)

#    Compute the Bhattacharyya coefficient.
   ct_db1_arr = np.array(ct_db1)
   ct_db2_arr = np.array(ct_db2)
   BC_val = np.sum(np.sqrt(ct_db1_arr*ct_db2_arr))

   return BC_val

def check_num_bins(ct_db1, ct_db2):
#     Checks if the number of bins for the two distributions are equal.  If
#     not, this funtion prints an error message and halts execution.
   import sys

   if len(ct_db1) != len(ct_db2):
      print("\n*** The two provided distributions do not have ***", sep='')
      print("\n*** the same number of bins. ***", sep='')
      print("*** Exiting. ***\n")
      sys.exit(1)

####

def normalize_dbns(ct_db1, ct_db2):
#    Normalizes the distribution counts so that they add up to 1.

#    This is the tolerance for floating point number differences.
#   fp_dif_tol = 1.e-5


   ct_db1_norm = ct_db1
   sum_ct_db1 = sum(ct_db1)
   if sum_ct_db1 != 1.0:
      print("-> Normalizing the first distribution.")
      ct_db1_norm = [ct/sum_ct_db1 for ct in ct_db1]

   ct_db2_norm = ct_db2
   sum_ct_db2 = sum(ct_db2)
   if sum_ct_db2 != 1.0:
      print("-> Normalizing the second distribution.")
      ct_db2_norm = [ct/sum_ct_db2 for ct in ct_db2]

   return (ct_db1_norm, ct_db2_norm)
