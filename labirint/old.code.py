                '''
                if (direction == 0):
                    if(w > 0):
                        self.labirint.mark('inc')
                        res = self.labirint.move('w')
                        self.move_count += 1
                        sig = res.get('sig')
                        print('sig=', sig)
                    else:
                        break
                elif (direction == 1):
                    if(s > 0):
                        self.labirint.mark('inc')
                        res = self.labirint.move('s')
                        self.move_count += 1
                        sig = res.get('sig')
                        print('sig=', sig)
                    else:
                        break
                elif (direction == 2):
                    if(e > 0):
                        self.labirint.mark('inc')
                        res = self.labirint.move('e')
                        self.move_count += 1
                        sig = res.get('sig')
                        print('sig=', sig)
                    else:
                        break
                elif (direction == 3):
                    if(n > 0):
                        self.labirint.mark('inc')
                        res = self.labirint.move('n')
                        self.move_count += 1
                        sig = res.get('sig')
                        print('sig=', sig)
                    else:
                        break
                '''
