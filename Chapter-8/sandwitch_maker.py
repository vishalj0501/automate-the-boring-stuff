import pyinputplus as pyp
def sandwitch():
    bread_type={'wheat':100,'white':120,'sourdough':140}
    protein_type={'chicken':50,'turkey':55,'ham':70,'tofu':75}
    cheese_type={'cheddar':40,'swiss':50,'mozzarella':75}
    extras_type={'mayo':15,'mustard':25,'lettuce':35,'tomato':45}

    total=0

    bread_in=pyp.inputMenu(list(bread_type.keys()))
    total+=bread_type[bread_in]

    protein_in=pyp.inputMenu(list(protein_type.keys()))
    total+=protein_type[protein_in]

    cheese_in1=pyp.inputYesNo("Do you want cheese: \n")
    if(cheese_in1=='yes'):
        cheese_in=pyp.inputMenu(list(cheese_type.keys()))
        total+=cheese_type[cheese_in]
    
    extras_in1=pyp.inputYesNo("Do you want extras(mayo,mustard,lettuce,tomato): \n")
    if(extras_in1=='yes'):
        extras_in=pyp.inputMenu(list(extras_type.keys()))
        total+=extras_type[extras_in]
    
    total_sand=pyp.inputInt("Enter the number of sandwitches: ")
    print("\nYour total bill is:\n $"+str(total_sand*total))
    

sandwitch()

