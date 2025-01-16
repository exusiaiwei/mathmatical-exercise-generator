import numpy as np
from fractions import Fraction

import formatters.latex_formatter

class MatrixProperties:
    @staticmethod
    def generate_from_rref(size):
        """Generate matrix with controlled properties"""
        def to_fraction_matrix(matrix):
            return np.array([[Fraction(int(x)) for x in row] for row in matrix])
        def to_augmented(matrix):
            # 创建增广矩阵 [A|I]
            aug = np.zeros((size, 2*size), dtype=Fraction)
            aug[:,:size] = matrix
            for i in range(size):
                aug[i,size+i] = Fraction(1)
            return aug

        def record_step(current, desc):
            return {
                'matrix': current.copy(),
                'description': desc
            }

        # 1. 生成目标秩和性质
        rank = np.random.randint(max(2, size-1), size+1)  # 保证秩至少为2

        # 2. 构建RREF形式（使用分数）
        rref = np.zeros((size, size), dtype=Fraction)
        for i in range(rank):
            rref[i,i] = Fraction(1)
            # 修改非零元素生成逻辑
            remaining_positions = size - i - 1
            if remaining_positions > 0:
                non_zero_count = np.random.randint(1, min(remaining_positions + 1, 3))
                positions = np.random.choice(range(i+1, size),
                                          min(non_zero_count, remaining_positions),
                                          replace=False)
                for j in positions:
                    while True:
                        val = np.random.randint(-2, 3)
                        if val != 0:
                            rref[i,j] = Fraction(val)
                            break

        # 3. 生成初等变换矩阵（保证可逆且元素简单）
        E = np.eye(size, dtype=Fraction)
        operations = []
        num_operations = np.random.randint(3, 5)  # 控制变换次数

        for _ in range(num_operations):
            i, j = np.random.choice(size, 2, replace=False)
            while True:
                c = Fraction(np.random.randint(-2, 3))
                if c != 0:
                    break
            E[i] = E[i] + c * E[j]
            operations.append((i, j, c))

        # 4. 计算原始矩阵和属性
        original = E @ rref
        matrix_rank = rank  # 我们知道确切的秩
        nullity = size - rank

        # 5. 计算行列式（通过E的性质）
        det = Fraction(1)
        for i in range(size):
            row_prod = Fraction(1)
            for j in range(size):
                row_prod *= E[i,j]
            det *= row_prod

        # 6. 计算逆矩阵（如果存在）
        inverse = None
        if rank == size:  # 满秩则可逆
            E_inv = np.linalg.inv(E.astype(float))
            inverse = to_fraction_matrix(E_inv)

        # 7. 计算kernel
        kernel = None
        if nullity > 0:
            kernel = np.zeros((size, nullity), dtype=Fraction)
            col = 0
            for i in range(size):
                if i >= rank:  # 非主元列
                    kernel[i,col] = Fraction(1)
                    for j in range(rank):
                        kernel[j,col] = -rref[j,i]
                    col += 1

        # 记录消元过程
        reduction_steps = []
        augmented = to_augmented(original)
        current = augmented.copy()

        # 记录初始状态
        reduction_steps.append(record_step(current, "Initial augmented matrix [A|I]"))

        # 进行消元
        for i in range(size):
            # 1. 找主元
            if abs(current[i,i]) < 1e-10:
                # 需要交换行
                for j in range(i+1, size):
                    if abs(current[j,i]) > 1e-10:
                        current[[i,j]] = current[[j,i]]
                        reduction_steps.append(record_step(current,
                            f"Swap row {i+1} and row {j+1}"))
                        break

            # 2. 主元归一
            if abs(current[i,i]) > 1e-10:
                pivot = current[i,i]
                if pivot != 1:
                    current[i] = current[i] / pivot
                    reduction_steps.append(record_step(current,
                        f"Multiply row {i+1} by {1/pivot}"))

                # 3. 消去其他行的对应元素
                for j in range(size):
                    if i != j and abs(current[j,i]) > 1e-10:
                        factor = current[j,i]
                        current[j] = current[j] - factor * current[i]
                        reduction_steps.append(record_step(current,
                            f"Subtract {factor} times row {i+1} from row {j+1}"))

        problem_str, answer_str = formatters.latex_formatter.format_matrix_properties_problem({
            'original': original,
            'rref': rref,
            'rank': matrix_rank,
            'nullity': nullity,
            'determinant': det,
            'inverse': inverse,
            'kernel': kernel,
            'augmented_steps': reduction_steps
        }, 1)
        return problem_str, answer_str

class RREFGenerator:
    @staticmethod
    def generate_rref_problem(size):
        def record_operation(ops, i, j, c):
            ops.append((i, j, c))
            return ops

        # 先生成RREF形式（确保简单合理）
        rref = np.zeros((size, size), dtype=Fraction)
        rank = np.random.randint(max(2, size-1), size+1)  # 保证秩至少为2

        # 构建简单的RREF
        for i in range(rank):
            rref[i,i] = Fraction(1)  # 主元为1
            # 在主元右侧可能添加一些非零元素
            for j in range(i+1, size):
                if np.random.random() < 0.3:  # 30%的概率添加非零元素
                    rref[i,j] = Fraction(np.random.randint(-2, 3))

        # 生成简单的初等行变换矩阵
        E = np.eye(size, dtype=Fraction)
        operations = []
        num_operations = np.random.randint(2, 4)  # 控制变换次数

        for _ in range(num_operations):
            i, j = np.random.choice(size, 2, replace=False)
            # 使用较小的系数（-2到2）
            c = Fraction(np.random.randint(-2, 3))
            while c == 0:
                c = Fraction(np.random.randint(-2, 3))
            # 记录操作
            operations.append((i, j, c))
            # 应用行变换
            E[i] = E[i] + c * E[j]

        # 计算原始矩阵
        original = E @ rref

        # 生成解答步骤（反向操作）
        steps = []
        intermediate_matrices = []
        current = original.copy()

        # 反向执行操作来达到RREF
        for i, j, c in operations[::-1]:
            step_desc = (
                f"Add {-c} times row {j+1} to row {i+1}"
                if c > 0 else
                f"Subtract {abs(c)} times row {j+1} from row {i+1}"
            )
            steps.append(step_desc)
            # 执行反向操作
            current = current.copy()
            current[i] = current[i] - c * current[j]
            intermediate_matrices.append(current.copy())

        return {
            'original': original,
            'rref': rref,
            'steps': steps,
            'intermediate_matrices': intermediate_matrices
        }
