# 4-Rod Weight Transfer Puzzle

This is a Python implementation of a CLI-based puzzle inspired by the Tower of Hanoi, but with an additional twist: **four rods** are used instead of the usual three. The goal of the game is to transfer all the weights (discs) from the first rod to any of the other rods, following a rule that you can't place a heavier weight on top of a lighter one.

## Game Rules

1. You start with all weights (discs) stacked in descending order (largest to smallest) on **Rod 1**.
2. The objective is to move all the weights from **Rod 1** to any of the other rods: **Rod 2, Rod 3, or Rod 4**.
3. You can only move **one weight at a time**.
4. You **cannot place a heavier weight on top of a lighter weight**.
5. The game is won once all weights are successfully transferred to one of the other rods.

## How to Play

1. When prompted, enter the rod number you'd like to move a weight **from** and the rod you'd like to move the weight **to**.
2. The rods are numbered from 1 to 4.
3. The current state of the rods is displayed after every move (successful or not), so you can keep track of your progress.
