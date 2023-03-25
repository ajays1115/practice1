def makes_model(g):
    di={a:b for a,b in zip(car_makes,g)}
    print(di)
car_makes=['Honda','Toyota','Ford','Nissan','Hyundai']
car_models=['Honda Civic','Honda Accord','Toyota Corolla','Toyota Camry','Ford Fusion','Ford Fusion','Ford Escape','Nissan Sentra','Hyundai Elantra']
g=[]
for key in car_makes:
    temp=[]
    for value in car_models:
        if key in value:
            temp.append(value)
    g.append(temp)
makes_model(g)

