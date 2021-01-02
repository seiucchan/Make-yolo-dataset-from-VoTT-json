import json

def json2txt(filename, maxnum):
    with open(file) as f:
        d = json.load(f)

    count = maxnum
    for id_name in d["assets"]:
      labels = []
      for i, data in enumerate(d["assets"][str(id_name)]['regions']):
        label = []
        for tag in d["assets"][str(id_name)]['regions'][i]['tags']:
            if tag == "person":
                tag = 0
            if tag == "ball":
                tag = 1
            label.append(tag)
        
        n = 0
        for point in d["assets"][str(id_name)]['regions'][i]['points']:
            if n == 0:
                x1 = point["x"]
                y1 = point["y"]

            if n == 2:
                x2 = point["x"]
                y2 = point["y"]
            n += 1    
        x_center = (x1 + (x2-x1)/2) / 1280
        x_center = format(x_center, '.6f')
        y_center = (y1 + (y2-y1)/2) / 720
        y_center = format(y_center, '.6f')
        label.append(x_center)
        label.append(y_center)
        
        w = d["assets"][str(id_name)]['regions'][i]['boundingBox']["width"] / 1280
        h = d["assets"][str(id_name)]['regions'][i]['boundingBox']["height"] / 720
        w = format(w, '.6f')
        h = format(h, '.6f')
        label.append(w)
        label.append(h)
        
        labels.append(label)
    
    for label in labels:
        print(label)
        c = 0
        for l in label:
            if c == 4:
                s = str(l)
                print(count, s)
                path_w = '{}/{}_{:0=5}.txt'.format(filename, filename, count)
                with open(path_w, mode='a') as f:
                    f.write(s)
                with open(path_w, mode='a') as f:
                    f.write("\n")
            else:
                s = str(l) + ' '
                print(count, s)
                path_w = '{}/{}_{:0=5}.txt'.format(filename, filename, count)
                with open(path_w, mode='a') as f:
                    f.write(s)

            c += 1
    count -= 1        