import ray
context = ray.init()
print(context.dashboard_url)

@ray.remote
def f(x):
    return x*x

futures=[ f.remote(i) for i in range(100)]
results= ray.get(futures)
print (results)