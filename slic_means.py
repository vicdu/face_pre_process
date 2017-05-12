def slic_means(img,segments):
    color=[1]*1500
    ind_array=[]

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            index=segments[i,j]
            if index in ind_array:
                img[i,j]=color[index][0]
            else:
                ind_array.append(index)
                color[index] = [img[i,j]]
    return img