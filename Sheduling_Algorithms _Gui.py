import tkinter as tk

root = tk.Tk()
root.title("SJF Scheduler")
root.geometry("1200x630+400+200")
root.title('Process scheduling')
root.resizable(False,False)
root.configure(bg='#3a5993')


frame1= tk.LabelFrame(root,font=20)
frame1.place(x=0,y=0)
def sjf_pre():
    tk.Label(frame1, text="Number of processes:",font=10).grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(frame1)
    entry1.grid(row=0, column=3, padx=10, pady=10)
    entries = []
    def show():
        global n
        n = int(entry1.get())
        bt = [0] * (n + 1)
        at = [0] * (n + 1)
        abt = [0] * (n + 1)
        labels = ['Burst Time', 'Arrival Time']
        
        for i in range(1, n+1):
            row=[]
            for j in range(2):
                label = tk.Label(frame1, text=labels[j] + ' for process ' + str(i) + ':')
                label.grid(row=i, column=j*2, padx=10, pady=10)
                entry = tk.Entry(frame1)
                entry.grid(row=i, column=j*2+1, padx=10, pady=10)
                row.append(entry)
            entries.append(row)
                
    
    output = tk.Text(frame1, height=10, width=50)
    output.grid(row=12, column=0, columnspan=4, padx=10, pady=10)       
    def clear():
       for entry in entries:
        entry[0].delete(0, tk.END)
        entry[1].delete(0, tk.END)
       output.delete('1.0', tk.END)       
    
    
    def calc():
        n = int(entry1.get())
        bt = [0] * (n + 1)
        at = [0] * (n + 1)
        abt = [0] * (n + 1)
        for i in range(n):
          abt[i] = int(entries[i][0].get())
          at[i] = int(entries[i][1].get())
          bt[i] = [abt[i], at[i], i]

        bt.pop(-1)
        sumbt = 0
        i = 0
        ll = []
        for i in range(0, sum(abt)):
           l = [j for j in bt  if j[1] <= i]
           l.sort(key=lambda x: x[0])
           bt[bt.index(l[0])][0] -= 1
           for k in bt:
               if k[0] == 0:
                  t = bt.pop(bt.index(k))
                  ll.append([k, i + 1])

        ct = [0] * (n + 1)
        tat = [0] * (n + 1)
        wt = [0] * (n + 1)
        for i in ll:
           ct[i[0][2]] = i[1]
        for i in range(len(ct)):
           tat[i] = ct[i] - at[i]
           wt[i] = tat[i] - abt[i]
        ct.pop(-1)
        wt.pop(-1)
        tat.pop(-1)
        abt.pop(-1)
        at.pop(-1)
        output.delete('1.0', tk.END)
        output.insert(tk.END, 'BT\tAT\tCT\tTAT\tWT\n')
        for i in range(len(ct)):
           output.insert(tk.END, "{}\t{}\t{}\t{}\t{}\n".format(abt[i], at[i], ct[i], tat[i], wt[i]))
        output.insert(tk.END, 'Average Waiting Time = {:.2f}\n'.format(sum(wt)/len(wt)))
        output.insert(tk.END, 'Average Turnaround Time = {:.2f}\n'.format(sum(tat)/len(tat)))
    button1 = tk.Button(frame1, text="calc",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993',  command=calc)
    button1.grid(row=13, column=0, padx=10, pady=10)
    button2 = tk.Button(frame1, text="Clear",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=clear)
    button2.grid(row=13, column=2, padx=10, pady=10)
    button1 = tk.Button(frame1, text="Enter",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=show)
    button1.grid(row=0, column=4, padx=10, pady=10)            
    button3 = tk.Button(frame1, text="Quit",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=frame1.destroy)
    button3.grid(row=13, column=3, padx=10, pady=10)

frame2= tk.LabelFrame(root,font=20)
frame2.place(x=0,y=0)
def fcfs():
    tk.Label(frame2, text="Number of processes:",font=20).grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(frame2)
    entry1.grid(row=0, column=3, padx=10, pady=10)
    
    bt = []
    at = []
    ct = []
    tat = []
    wt = []
    entries = []
    def show():
        global n
        n = int(entry1.get())
        
        labels = ['Burst Time', 'Arrival Time']
        
        for i in range(1, n+1):
            row=[]
            for j in range(2):
                label = tk.Label(frame2, text=labels[j] + ' for process ' + str(i) + ':')
                label.grid(row=i, column=j*2, padx=10, pady=10)
                entry = tk.Entry(frame2)
                entry.grid(row=i, column=j*2+1, padx=10, pady=10)
                row.append(entry)
            entries.append(row)
                
    
    output = tk.Text(frame2, height=10, width=50)
    output.grid(row=12, column=0, columnspan=4, padx=10, pady=10)       
    def clear():
       for entry in entries:
        entry[0].delete(0, tk.END)
        entry[1].delete(0, tk.END)
       output.delete('1.0', tk.END)
    def calc():
        for i in range(n):
            bt.append(int(entries[i][0].get()))
            at.append(int(entries[i][1].get()))

        ct.append(at[0] + bt[0])
        tat.append(ct[0] - at[0])
        wt.append(tat[0] - bt[0])
        for i in range(1, n):
            ct.append(at[i] + bt[i] + ct[i-1] - max(ct[i-1], at[i]))
            tat.append(ct[i] - at[i])
            wt.append(tat[i] - bt[i])

        avg_tat = sum(tat) / n
        avg_wt = sum(wt) / n
        output.delete('1.0', tk.END)
        output.insert(tk.END, 'Process\tBT\tAT\tCT\tTAT\tWT\n')
        for i in range(n):
            output.insert(tk.END, f"P{i+1}\t{bt[i]}\t{at[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\n")
        output.insert(tk.END, f"Average Turnaround Time: {avg_tat:.2f}\n")
        output.insert(tk.END, f"Average Waiting Time: {avg_wt:.2f}\n")
    button1 = tk.Button(frame2, text="calc",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993',  command=calc)
    button1.grid(row=13, column=0, padx=10, pady=10)
    button2 = tk.Button(frame2, text="Clear",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=clear)
    button2.grid(row=13, column=2, padx=10, pady=10)
    button1 = tk.Button(frame2, text="Enter",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=show)
    button1.grid(row=0, column=4, padx=10, pady=10)            
    button3 = tk.Button(frame2, text="Quit",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=frame2.destroy)
    button3.grid(row=13, column=3, padx=10, pady=10)
frame3= tk.LabelFrame(root,font=20)
frame3.place(x=0,y=0)
def sjf_nonpre():
    tk.Label(frame3, text="Number of processes:",font=20).grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(frame3)
    entry1.grid(row=0, column=3, padx=10, pady=10)
    
    bt = []
    at = []
    ct = []
    tat = []
    wt = []
    entries = []
    def show():
        global n
        n = int(entry1.get())
        bt = [0] * (n + 1)
        at = [0] * (n + 1)
        abt = [0] * (n + 1)
        labels = ['Burst Time', 'Arrival Time']
        
        for i in range(1, n+1):
            row=[]
            for j in range(2):
                label = tk.Label(frame3, text=labels[j] + ' for process ' + str(i) + ':')
                label.grid(row=i, column=j*2, padx=10, pady=10)
                entry = tk.Entry(frame3)
                entry.grid(row=i, column=j*2+1, padx=10, pady=10)
                row.append(entry)
            entries.append(row)
                
    
    output = tk.Text(frame3, height=10, width=50)
    output.grid(row=12, column=0, columnspan=4, padx=10, pady=10)       
    def clear():
       for entry in entries:
        entry[0].delete(0, tk.END)
        entry[1].delete(0, tk.END)
       output.delete('1.0', tk.END)      
    def calc():
        for i in range(n):
            bt.append(int(entries[i][0].get()))
            at.append(int(entries[i][1].get()))

        remaining_bt = bt.copy()

    # Sort processes by burst time
        processes = sorted(list(enumerate(bt)), key=lambda x: x[1])

        ct.append(processes[0][1])
        tat.append(ct[0] - at[processes[0][0]])
        wt.append(tat[0] - bt[processes[0][0]])
        for i in range(1, n):
           ct.append(processes[i][1] + ct[i-1])
           tat.append(ct[i] - at[processes[i][0]])
           wt.append(tat[i] - bt[processes[i][0]])

        avg_tat = sum(tat) / n
        avg_wt = sum(wt) / n

        output.delete('1.0', tk.END)
        output.insert(tk.END, 'Process\tBT\tAT\tCT\tTAT\tWT\n')
        for i in range(n):
          output.insert(tk.END, f"P{processes[i][0]+1}\t{bt[processes[i][0]]}\t{at[processes[i][0]]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\n")
        output.insert(tk.END, f"Average Turnaround Time: {avg_tat:.2f}\n")
        output.insert(tk.END, f"Average Waiting Time: {avg_wt:.2f}\n")
    button1 = tk.Button(frame3, text="calc",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993',  command=calc)
    button1.grid(row=13, column=0, padx=10, pady=10)
    button2 = tk.Button(frame3, text="Clear",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=clear)
    button2.grid(row=13, column=2, padx=10, pady=10)
    button1 = tk.Button(frame3, text="Enter",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=show)
    button1.grid(row=0, column=4, padx=10, pady=10)            
    button3 = tk.Button(frame3, text="Quit",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=frame3.destroy)
    button3.grid(row=13, column=3, padx=10, pady=10)

frame4= tk.LabelFrame(root,font=20)
frame4.place(x=0,y=0)
def Round_robin():
    tk.Label(frame4, text="Number of processes:").grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(frame4)
    entry1.grid(row=0, column=3, padx=10, pady=10)
    tk.Label(frame4, text="Quantum size:").grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(frame4)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    bt = []
    at = []
    
    entries=[]
    
    def show():
        global n
        global quantum
        n = int(entry1.get())
        quantum = int(entry2.get())
        ct = [0] * n
        tat = [0] * n
        wt = [0] * n
        
        labels = ['Burst Time', 'Arrival Time']
        
        for i in range(1, n+1):
            row=[]
            for j in range(2):
                label = tk.Label(frame4, text=labels[j] + ' for process ' + str(i) + ':')
                label.grid(row=i, column=j*2, padx=10, pady=10)
                entry = tk.Entry(frame4)
                entry.grid(row=i, column=j*2+1, padx=10, pady=10)
                row.append(entry)
            entries.append(row)
                
    
    output = tk.Text(frame4, height=10, width=50)
    output.grid(row=12, column=0, columnspan=4, padx=10, pady=10)       
    def clear():
       for entry in entries:
        entry[0].delete(0, tk.END)
        entry[1].delete(0, tk.END)
       output.delete('1.0', tk.END) 
    def calc():
       ct = [0] * n
       tat = [0] * n
       wt = [0] * n
       for i in range(n):
           bt.append(int(entries[i][0].get()))
           at.append(int(entries[i][1].get()))

       remaining_bt = bt.copy()
       time = 0
       while True:
           done = True
           for i in range(n):
               if remaining_bt[i] > 0:
                   done = False
                   if remaining_bt[i] > quantum:
                       time += quantum
                       remaining_bt[i] -= quantum
                   else:
                       time += remaining_bt[i]
                       ct[i] = time
                       tat[i] = ct[i] - at[i]
                       wt[i] = tat[i] - bt[i]
                       remaining_bt[i] = 0
           if done:
               break

       output.delete('1.0', tk.END)
       output.insert(tk.END, 'Process\tBT\tAT\tCT\tTAT\tWT\n')
       for i in range(n):
           output.insert(tk.END, f"P{i+1}\t{bt[i]}\t{at[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}\n")
       output.insert(tk.END, f"Average Turnaround Time: {sum(tat) / n:.2f}\n")
       output.insert(tk.END, f"Average Waiting Time: {sum(wt) / n:.2f}\n")
        
        
    button1 = tk.Button(frame4, text="calc",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993',  command=calc)
    button1.grid(row=13, column=0, padx=10, pady=10)
    button2 = tk.Button(frame4, text="Clear",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=clear)
    button2.grid(row=13, column=2, padx=10, pady=10)
    button1 = tk.Button(frame4, text="Enter",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=show)
    button1.grid(row=0, column=4, padx=10, pady=10)            
    button3 = tk.Button(frame4, text="Quit",font=('times',10,'bold'),width=8  ,foreground='#ffffff' ,bg='#3a5993', command=frame4.destroy)
    button3.grid(row=13, column=3, padx=10, pady=10)


frame= tk.LabelFrame(root,text="Choose The Algorithm",padx=20,bg="#abc2ec",font=20)
frame.place(x=900,y=10)

button3 = tk.Button(frame, text="sjf_pre",font=('times',20,'bold'),width=15  ,foreground='#ffffff' ,bg='#3a5993', command=sjf_pre)
button3.grid(row=0, column=0, padx=0, pady=40)
button3 = tk.Button(frame, text="fcfs",font=('times',20,'bold'),width=15  ,foreground='#ffffff' ,bg='#3a5993', command=fcfs)
button3.grid(row=10, column=0, padx=0, pady=40)
button3 = tk.Button(frame, text="sjf_nonpre",font=('times',20,'bold'),width=15  ,foreground='#ffffff' ,bg='#3a5993',command=sjf_nonpre)
button3.grid(row=15, column=0, padx=0, pady=40)

button3 = tk.Button(frame, text="Round_robin",font=('times',20,'bold'),width=15  ,foreground='#ffffff' ,bg='#3a5993', command=Round_robin)
button3.grid(row=20, column=0, padx=0, pady=40)
root.mainloop()