from matplotlib import pyplot as plt
import pandas as py
import pandas as pd

df=pd.read_csv("tabular.csv")

def regression_report():
  print(df)
  x = list(sorted(df['runs.build'].unique()))
  ret = datesep(x)
  print ("<regression_report>", ret)
  return ret


def datesep(x):
    y=list(range(len(x)))
    plt.xticks(y,x)

    ax=df[df['failures.failStatus']=='F'].groupby('runs.build')['failures.failStatus'].count().reset_index(name='Number of Failures').head(10).plot(kind="bar",width=0.15)
    plt.setp(ax.get_xticklabels(),rotation=15,horizontalalignment='right')
    ax.set_xticklabels(labels=x,fontsize="small")

    plt.savefig('spir.png',dpi=1000)
    plt.title('Analysis Graph')
    plt.xlabel('builds')
    plt.ylabel('failures')
    plt.show()
    return
