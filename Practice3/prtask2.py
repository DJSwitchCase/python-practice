class C32:
    condition = 'A'
    number = 0
    def mass(self):
        try:
            if self.condition == 'A':
                self.condition = 'B'
                return 0
            elif self.condition == 'B':
                self.condition = 'F'
                return 2
            elif self.condition == 'E':
                self.condition = 'G'
                return 6
            elif self.condition == 'F':
                self.condition = 'G'
                return 7
            elif self.condition == 'G':
                self.condition = 'H'
                return 9
            else:
                raise RuntimeError
        except RuntimeError as e:
            print('RuntimeError')
    def leer(self):
            if self.condition == 'B':
                self.condition = 'C'
                return 1
            elif self.condition == 'C':
                self.condition = 'D'
                return 3
            elif self.condition == 'D':
                self.condition = 'E'
                return 4
            elif self.condition == 'E':
                self.condition = 'F'
                return 5
            elif self.condition == 'G':
                self.condition = 'C'
                return 10
            elif self.condition == 'H':
                self.condition = 'C'
                return 11
            elif self.condition == 'F':
                self.condition = 'C'
                return 8

