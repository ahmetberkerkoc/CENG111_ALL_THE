import math 
def linear_layer(layer_in,weight):
    out=[]
    for w in weight:
        x = [a*b for a,b in zip(layer_in,w)]
        out.append(sum(x))
    return out

def relu(layer_in):
    out = []
    for element in layer_in:
        if element <=0:
            out.append(0)
        else:
            out.append(element)
    return out

def sigmoid(layer_in):
    out=[]
    for element in layer_in:
        if element<=-700:
            out.append(0)
        elif element >=700:
            out.append(1)
        else:
            out.append(1/(1+math.exp(-element)))
    return out

def forward_pass(network1, X_sample):
    layer_out = X_sample[:]
    for i,layer in enumerate(network1):
        if type(layer)==list:
            if "linear" in layer[0]:
                weight = layer[1]
                layer_out = linear_layer(layer_out,weight)
        elif "relu" in layer:
            layer_out=relu(layer_out)
        elif "sigmoid" in layer:
            layer_out=sigmoid(layer_out)
    return layer_out
                
    


