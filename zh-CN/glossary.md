# MIT 6.004 汉化术语表

本术语表用于统一后续资料翻译。原则是：专业术语保持一致，课程专有名词不过度意译，代码、信号名、寄存器名、文件名和命令保持英文原样。

## 使用规则

1. 首次出现的重要术语可以写成“中文（English）”，后续只用中文。
2. `Beta`、`CMOS`、`MOSFET`、`ISA`、`FSM` 等课程专有名词或常用缩写保留英文。
3. 代码、命令、路径、文件名、寄存器名、信号名、模块名、测试名不翻译。
4. 数学公式、逻辑表达式和真值表结构不翻译，只翻译说明文字。
5. 同一个英文术语在同一语境下固定使用同一个中文译法。

## 课程与通用术语

| English | 中文建议 | 备注 |
| --- | --- | --- |
| MIT 6.004 | MIT 6.004 | 课程编号保留 |
| Computation Structures | 计算结构 | 课程名称 |
| computation | 计算 | |
| abstraction | 抽象 | |
| model | 模型 | |
| system | 系统 | |
| component | 组件 | |
| module | 模块 | 代码和电路模块名不翻译 |
| interface | 接口 | |
| implementation | 实现 | |
| specification | 规约 | 或“规格说明”，按语境选择 |
| behavior | 行为 | |
| correctness | 正确性 | |
| performance | 性能 | |
| tradeoff | 权衡 | |
| latency | 延迟 | |
| throughput | 吞吐量 | |
| bandwidth | 带宽 | |
| overhead | 开销 | |

## 信息与数字抽象

| English | 中文建议 | 备注 |
| --- | --- | --- |
| information | 信息 | |
| bit | 位 | |
| byte | 字节 | |
| word | 字 | 体系结构语境 |
| binary | 二进制 | |
| hexadecimal | 十六进制 | |
| encoding | 编码 | |
| representation | 表示 | |
| signal | 信号 | 具体信号名不翻译 |
| analog | 模拟 | 与 digital 相对 |
| digital | 数字 | 与 analog 相对 |
| digital abstraction | 数字抽象 | |
| valid range | 有效范围 | |
| noise margin | 噪声容限 | |
| threshold | 阈值 | |
| voltage | 电压 | |
| current | 电流 | |
| power | 功耗 | 电路语境 |
| energy | 能量 | |

## 布尔逻辑与组合逻辑

| English | 中文建议 | 备注 |
| --- | --- | --- |
| Boolean algebra | 布尔代数 | |
| Boolean expression | 布尔表达式 | |
| truth table | 真值表 | |
| logic gate | 逻辑门 | |
| inverter | 反相器 | |
| NOT gate | NOT 门 | |
| AND gate | AND 门 | |
| OR gate | OR 门 | |
| NAND gate | NAND 门 | |
| NOR gate | NOR 门 | |
| XOR gate | XOR 门 | |
| combinational logic | 组合逻辑 | |
| combinational circuit | 组合电路 | |
| minterm | 最小项 | |
| Karnaugh map | 卡诺图 | |
| K-map | K-map | 保留常用缩写 |
| simplification | 化简 | |
| multiplexer | 多路选择器 | 可简称 MUX |
| MUX | MUX | 保留英文缩写 |
| decoder | 译码器 | |
| encoder | 编码器 | |
| adder | 加法器 | |
| full adder | 全加器 | |
| carry | 进位 | |
| carry-in | 进位输入 | |
| carry-out | 进位输出 | |
| arithmetic logic unit | 算术逻辑单元 | 可简称 ALU |
| ALU | ALU | 保留英文缩写 |

## CMOS 与电路时序

| English | 中文建议 | 备注 |
| --- | --- | --- |
| CMOS | CMOS | 保留英文 |
| MOSFET | MOSFET | 保留英文 |
| transistor | 晶体管 | |
| nMOS | nMOS | 保留英文 |
| pMOS | pMOS | 保留英文 |
| pullup network | 上拉网络 | |
| pulldown network | 下拉网络 | |
| switch | 开关 | 电路语境 |
| capacitance | 电容 | |
| load capacitance | 负载电容 | |
| propagation delay | 传播延迟 | |
| contamination delay | 污染延迟 | |
| rising edge | 上升沿 | |
| falling edge | 下降沿 | |
| timing analysis | 时序分析 | |
| critical path | 关键路径 | |
| setup time | 建立时间 | |
| hold time | 保持时间 | |
| clock period | 时钟周期 | |
| clock frequency | 时钟频率 | |

## 时序逻辑与状态机

| English | 中文建议 | 备注 |
| --- | --- | --- |
| sequential logic | 时序逻辑 | |
| sequential circuit | 时序电路 | |
| state | 状态 | |
| state transition | 状态转移 | |
| finite state machine | 有限状态机 | 可简称 FSM |
| FSM | FSM | 保留英文缩写 |
| state diagram | 状态图 | |
| next state | 下一状态 | |
| current state | 当前状态 | |
| output logic | 输出逻辑 | |
| latch | 锁存器 | |
| flip-flop | 触发器 | |
| D flip-flop | D 触发器 | |
| register | 寄存器 | |
| register file | 寄存器文件 | |
| memory element | 存储元件 | |
| clock | 时钟 | |
| reset | 复位 | |
| synchronous | 同步的 | |
| asynchronous | 异步的 | |

## ISA、汇编与 Beta

| English | 中文建议 | 备注 |
| --- | --- | --- |
| instruction set architecture | 指令集架构 | 可简称 ISA |
| ISA | ISA | 保留英文缩写 |
| instruction | 指令 | |
| opcode | 操作码 | |
| operand | 操作数 | |
| immediate | 立即数 | |
| literal | 字面量 | |
| assembly language | 汇编语言 | |
| assembler | 汇编器 | |
| machine code | 机器码 | |
| program counter | 程序计数器 | 可简称 PC |
| PC | PC | 保留寄存器缩写 |
| register | 寄存器 | |
| memory address | 内存地址 | |
| load | 载入 | 指令语境 |
| store | 存储 | 指令语境 |
| branch | 分支 | |
| jump | 跳转 | |
| procedure | 过程 | 课程语境优先译为“过程” |
| subroutine | 子程序 | |
| stack | 栈 | |
| stack pointer | 栈指针 | |
| calling convention | 调用约定 | |
| activation record | 活动记录 | |
| Beta | Beta | 课程处理器名称，保留英文 |
| Beta processor | Beta 处理器 | |
| datapath | 数据通路 | |
| control logic | 控制逻辑 | |
| control signal | 控制信号 | 具体信号名不翻译 |
| control ROM | 控制 ROM | |
| microarchitecture | 微架构 | |

## 编译器与计算模型

| English | 中文建议 | 备注 |
| --- | --- | --- |
| compiler | 编译器 | |
| compilation | 编译 | |
| source code | 源代码 | |
| target code | 目标代码 | |
| parser | 解析器 | |
| syntax | 语法 | |
| semantics | 语义 | |
| expression | 表达式 | |
| statement | 语句 | |
| variable | 变量 | |
| environment | 环境 | |
| model of computation | 计算模型 | |
| Turing machine | 图灵机 | |
| universal machine | 通用机器 | |
| decidability | 可判定性 | |
| halting problem | 停机问题 | |

## 流水线

| English | 中文建议 | 备注 |
| --- | --- | --- |
| pipeline | 流水线 | |
| pipelining | 流水线化 | |
| pipeline stage | 流水级 | |
| stage register | 级间寄存器 | |
| instruction fetch | 取指 | |
| decode | 译码 | |
| execute | 执行 | |
| memory stage | 访存级 | |
| writeback | 写回 | |
| hazard | 冒险 | 流水线语境 |
| data hazard | 数据冒险 | |
| control hazard | 控制冒险 | |
| structural hazard | 结构冒险 | |
| stall | 停顿 | |
| bubble | 气泡 | 流水线空操作 |
| bypassing | 旁路 | |
| forwarding | 转发 | |
| branch prediction | 分支预测 | |
| speculation | 推测执行 | 如出现 |

## 缓存与存储层次

| English | 中文建议 | 备注 |
| --- | --- | --- |
| memory hierarchy | 存储层次结构 | |
| cache | 缓存 | |
| cache line | 缓存行 | |
| block | 块 | 缓存语境 |
| word | 字 | 缓存/体系结构语境 |
| hit | 命中 | |
| miss | 未命中 | |
| hit rate | 命中率 | |
| miss rate | 未命中率 | |
| miss penalty | 未命中代价 | |
| direct-mapped cache | 直接映射缓存 | |
| set-associative cache | 组相联缓存 | |
| fully associative cache | 全相联缓存 | |
| tag | 标记 | 缓存语境 |
| index | 索引 | 缓存语境 |
| offset | 偏移 | |
| valid bit | 有效位 | |
| dirty bit | 脏位 | |
| replacement policy | 替换策略 | |
| least recently used | 最近最少使用 | 可简称 LRU |
| LRU | LRU | 保留英文缩写 |
| write-through | 直写 | |
| write-back | 写回 | 缓存策略 |
| cache coherence | 缓存一致性 | |
| coherence protocol | 一致性协议 | |

## 虚拟内存与操作系统

| English | 中文建议 | 备注 |
| --- | --- | --- |
| virtual memory | 虚拟内存 | |
| virtual address | 虚拟地址 | |
| physical address | 物理地址 | |
| address translation | 地址转换 | |
| page | 页 | |
| page table | 页表 | |
| page table entry | 页表项 | 可简称 PTE |
| PTE | PTE | 保留英文缩写 |
| page fault | 缺页异常 | |
| translation lookaside buffer | 地址转换后备缓冲区 | 可简称 TLB |
| TLB | TLB | 保留英文缩写 |
| protection | 保护 | OS/内存语境 |
| privilege | 特权 | |
| kernel | 内核 | |
| user mode | 用户模式 | |
| kernel mode | 内核模式 | |
| operating system | 操作系统 | |
| process | 进程 | |
| context switch | 上下文切换 | |
| virtualization | 虚拟化 | |
| virtualizing the processor | 处理器虚拟化 | |

## 中断、设备与系统通信

| English | 中文建议 | 备注 |
| --- | --- | --- |
| interrupt | 中断 | |
| exception | 异常 | |
| illegal instruction | 非法指令 | |
| device | 设备 | |
| I/O | I/O | 保留英文缩写 |
| input/output | 输入/输出 | |
| memory-mapped I/O | 内存映射 I/O | |
| device driver | 设备驱动程序 | |
| polling | 轮询 | |
| interrupt handler | 中断处理程序 | |
| trap | 陷入 | OS/异常语境 |
| bus | 总线 | |
| protocol | 协议 | |
| packet | 数据包 | |
| network | 网络 | |
| system-level communication | 系统级通信 | |

## 并发、同步与并行

| English | 中文建议 | 备注 |
| --- | --- | --- |
| concurrency | 并发 | |
| synchronization | 同步 | |
| parallel processing | 并行处理 | |
| thread | 线程 | |
| race condition | 竞争条件 | |
| critical section | 临界区 | |
| mutual exclusion | 互斥 | |
| lock | 锁 | |
| semaphore | 信号量 | |
| deadlock | 死锁 | |
| atomic operation | 原子操作 | |
| test-and-set | 测试并设置 | |
| shared memory | 共享内存 | |
| message passing | 消息传递 | |
| speedup | 加速比 | |
| load balancing | 负载均衡 | |

## 实验与工具常用词

| English | 中文建议 | 备注 |
| --- | --- | --- |
| lab | 实验 | |
| worksheet | 练习题 | |
| checkoff | 验收 | 课程实验语境 |
| template | 模板 | 文件名不翻译 |
| sandbox | 沙盒 | 工具页面语境 |
| simulation | 仿真 | |
| simulator | 仿真器 | |
| waveform | 波形 | |
| schematic | 原理图 | |
| netlist | 网表 | |
| test case | 测试用例 | |
| test bench | 测试平台 | |
| module library | 模块库 | |
| Jade | Jade | 工具名保留 |
| JSim | JSim | 工具名保留 |
| BSim | BSim | 工具名保留 |
| TMSim | TMSim | 工具名保留 |

## 不翻译清单

- 代码块、内联代码、命令行示例。
- 文件名和路径，例如 `template.uasm`、`checkoff.json`、`labs/lab1_cmos/lab.html`。
- 寄存器名、信号名、模块名、测试名。
- 工具名和课程处理器名，例如 `Beta`、`Jade`、`JSim`、`BSim`、`TMSim`。
- 常用缩写：`CMOS`、`MOSFET`、`ISA`、`FSM`、`ALU`、`PC`、`TLB`、`PTE`、`LRU`、`I/O`。

## 风格约定

- 讲义：准确、清晰，保留原有逻辑层次。
- 实验：步骤化、可执行，避免把命令或文件名误翻译。
- Worksheet：题意自然，保留编号、变量和公式。
- PPTX：中文尽量短，优先避免文本框溢出。
