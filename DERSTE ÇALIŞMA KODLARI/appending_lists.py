#%%


def make_2d_arr(rows, columns):
    lst = [ ['#' for col in range(columns)] for row in range(rows)] 
    return lst


lisst = make_2d_arr(1,2)
print(lisst)

lisst.append(lisst)
print(lisst)

# %%
