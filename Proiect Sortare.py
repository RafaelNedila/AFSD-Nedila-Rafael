class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Vizualizator Algoritmi de Sortare")
        self.root.geometry("800x600")
        

        self.algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Bogo Sort"]
        self.selected_algorithm = tk.StringVar(value=self.algorithms[0])
        self.num_elements = tk.IntVar(value=20)
        self.speed = tk.DoubleVar(value=0.5)
        self.data = []

 
        self.create_ui()

    def create_ui(self):
      
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        
        tk.Label(control_frame, text="Algoritm:").grid(row=0, column=0, padx=5, pady=5)
        algorithm_menu = ttk.Combobox(control_frame, textvariable=self.selected_algorithm, values=self.algorithms, state="readonly")
        algorithm_menu.grid(row=0, column=1, padx=5, pady=5)

        
        tk.Label(control_frame, text="Număr elemente:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(control_frame, textvariable=self.num_elements).grid(row=1, column=1, padx=5, pady=5)

        
        tk.Label(control_frame, text="Viteză animație:").grid(row=2, column=0, padx=5, pady=5)
        speed_slider = ttk.Scale(control_frame, from_=0.1, to=2.0, variable=self.speed)
        speed_slider.grid(row=2, column=1, padx=5, pady=5)

       
        tk.Button(control_frame, text="Generează Date", command=self.generate_data).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(control_frame, text="Începe Sortarea", command=self.start_sorting).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(control_frame, text="Reset", command=self.reset).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(control_frame, text="Ieșire", command=self.root.quit).grid(row=4, column=1, padx=5, pady=5)

        
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def generate_data(self):
        num_elements = self.num_elements.get()
        self.data = random.sample(range(1, 100), num_elements)
        self.draw_bars(self.data)

    def draw_bars(self, data, colors=None):
        self.canvas.delete("all")
        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(data)
        max_height = max(data)

        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = canvas_height - (value / max_height) * canvas_height
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            color = colors[i] if colors else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
            self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(value), font=("Arial", 10))

        self.root.update_idletasks()

    def start_sorting(self):
        algorithm = self.selected_algorithm.get()
        if algorithm == "Bubble Sort":
            self.bubble_sort(self.data)
        elif algorithm == "Insertion Sort":
            self.insertion_sort(self.data)
        elif algorithm == "Selection Sort":
            self.selection_sort(self.data)
        elif algorithm == "Bogo Sort":
            self.bogo_sort(self.data)

    def bubble_sort(self, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                self.draw_bars(data, ["red" if x == j or x == j + 1 else "blue" for x in range(len(data))])
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                self.root.after(int(self.speed.get() * 1000))
        self.draw_bars(data, ["green"] * len(data))

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                self.draw_bars(data, ["red" if x == j or x == j + 1 else "blue" for x in range(len(data))])
                data[j + 1] = data[j]
                j -= 1
                self.root.after(int(self.speed.get() * 1000))
            data[j + 1] = key
        self.draw_bars(data, ["green"] * len(data))

    def selection_sort(self, data):
        for i in range(len(data)):
            min_idx = i
            for j in range(i + 1, len(data)):
                self.draw_bars(data, ["red" if x == j or x == min_idx else "blue" for x in range(len(data))])
                if data[j] < data[min_idx]:
                    min_idx = j
                self.root.after(int(self.speed.get() * 1000))
            data[i], data[min_idx] = data[min_idx], data[i]
        self.draw_bars(data, ["green"] * len(data))

    def bogo_sort(self, data):
        while not self.is_sorted(data):
            random.shuffle(data)
            self.draw_bars(data, ["red"] * len(data))
            self.root.after(int(self.speed.get() * 1000))
        self.draw_bars(data, ["green"] * len(data))

    @staticmethod
    def is_sorted(data):
        return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

    def reset(self):
        self.data = []
        self.canvas.delete("all")



