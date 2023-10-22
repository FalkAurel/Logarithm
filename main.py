from logic import ln, lnOptimized
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 15, 25)
y = np.log(x)
yhatLNO = np.apply_along_axis(lnOptimized, 0, x)
yhatLN = np.apply_along_axis(ln, 0, x)

def error(yhat, y):
    """
    Returns the RSS and the RMSE
    """
    RSS = np.square(y - yhat).sum()
    RMSE = np.mean(np.square(y - yhat))**0.5
    return RSS, RMSE

_, (axis1, axis2) = plt.subplots(nrows=2, ncols=1)
axis1.plot(x, y, "o-", label="np.log")
axis1.plot(x, yhatLN, "o-", label="ln [precision set to 20]")
axis1.set_xlabel("X")
axis1.set_ylabel("y")
RSS, RMSE = error(yhatLN, y)
axis1.set_title(f"""RSS : {RSS}
RMSE : {RMSE}""")
axis1.legend()
axis2.plot(x, y, "o-", label="np.log")
axis2.plot(x, yhatLNO, "o-", label="lnOptimized [precision set to 20]")
axis2.set_xlabel("X")
axis2.set_ylabel("y")
RSS, RMSE = error(yhatLNO, y)
axis2.set_title(f"""RSS : {RSS}
RMSE : {RMSE}""")
axis2.legend()
plt.tight_layout()
plt.show()