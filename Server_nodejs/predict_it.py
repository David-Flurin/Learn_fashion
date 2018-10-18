import test_network as tn 
import sys

pred = tn.Prediction(sys.argv[1])
print(pred.predict_img())