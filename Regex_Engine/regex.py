import sys

sys.setrecursionlimit(10000)


class RegEx:

    def main(self):
        self.initial_user_input = input().split("|")
        self.regex = self.initial_user_input[0]
        self.initial_regex = self.regex
        self.pair = self.initial_user_input[1]
        self.initial_pair = self.pair
        self.regex_length = len(self.regex)
        self.pair_length = len(self.pair)
        if self.edge_case():
            print(self.verification_loop())
        else:
            print("False")

    def edge_case(self):
        if "^" in self.regex and "$" in self.regex:
            if self.regex[1] == self.pair[0]:
                if (self.regex[-2] == self.pair[-1] or self.regex[-2] == ".") and (
                        len(self.regex[1:len(self.regex) - 1]) == len(self.pair)):
                    self.regex = self.regex[2:len(self.regex) - 1]
                    self.pair = self.pair[1::]
                    return True
        elif "^" in self.regex:
            if self.regex[1] == self.pair[0]:
                self.regex = self.regex[2::]
                self.pair = self.pair[1::]
                return True
            else:
                return False
        elif "$" in self.regex:
            if self.regex[-2] == self.pair[-1] or self.regex[-2] == ".":
                self.regex = self.regex[0:len(self.regex) - 1]
                return True
            else:
                return False
        elif "^" not in self.regex or "$" not in self.regex:
            return True
        else:
            return False

    def controlling_repetition(self):
        if self.regex[0] == self.pair[0] and self.regex[0] == self.pair[1]:
            return False
        elif self.regex[0] == self.pair[0]:
            self.regex = self.regex[2::]
            self.pair = self.pair[1::]
        elif self.regex[0] != self.pair[0]:
            self.regex = self.regex[2::]

    def reverse_regex(self):
        if "^" in self.initial_regex:
            self.regex = self.initial_regex[1::]
        if "$" in self.regex:
            self.regex = self.regex[0:len(self.regex) - 1]

    def verification_loop(self):
        if len(self.regex) == 0:
            return True
        elif len(self.pair) == 0:
            return False
        elif len(self.regex) > 2 and self.regex[1] == "?":
            if self.regex[0] == self.pair[0] and self.regex[0] == self.pair[1]:
                return False
            elif self.regex[0] == self.pair[0]:
                self.regex = self.regex[2::]
                self.pair = self.pair[1::]
                return self.verification_loop()
            elif self.regex[0] != self.pair[0]:
                self.regex = self.regex[2::]
                return self.verification_loop()
        elif len(self.regex) > 2 and self.regex[1] == "*":
            if self.regex[0] == self.pair[0] and self.regex[0] == self.pair[1]:
                if self.regex[0] == self.pair[1]:
                    print("yes")
                    counter = 0
                    for i in range(len(self.pair)):
                        while self.regex[0] == self.pair[i]:
                            counter += 1
                        self.regex = self.regex[2::]
                        self.pair = self.pair[counter+1::]
                    return self.verification_loop()
                else:
                    self.regex = self.regex[2::]
                    self.pair = self.pair[1::]
                    return self.verification_loop()
            elif self.regex[0] != self.pair[0]:
                self.regex = self.regex[2::]
                return self.verification_loop()
            elif self.regex[0] == self.pair[0] and self.regex[0] != self.pair[1]:
                self.regex = self.regex[2::]
                self.pair = self.pair[1::]
                return self.verification_loop()
        elif self.regex[0] == ".":
            self.regex = self.regex[1::]
            self.pair = self.pair[1::]
            return self.verification_loop()
        elif self.regex[0] == self.pair[0]:
            self.regex = self.regex[1::]
            self.pair = self.pair[1::]
            return self.verification_loop()
        elif self.regex[0] != self.pair[0]:
            if len(self.regex) < len(self.pair):
                self.reverse_regex()
                if self.regex[0] == self.pair[0]:
                    self.regex = self.regex[1::]
                    self.pair = self.pair[1::]
                    return self.verification_loop()
                else:
                    self.pair = self.pair[1::]
                    return self.verification_loop()
            else:
                return False


test_run = RegEx()
test_run.main()

