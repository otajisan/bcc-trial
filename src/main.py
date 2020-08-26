#!/usr/bin/python
# -*- coding: utf-8 -*-

from bcc import BPF

prog = """
int trace_sys_clone(struct pt_regs *ctx) {
  bpf_trace_printk("Hello, World!\\n");
  return 0;
}
"""


def main(debug=0):
    #debug=0x8
    bpf = BPF(text=prog, debug=debug)
    # watch __x64_sys_clone execution on kernel
    bpf.attach_kprobe(event='sys_clone', fn_name='trace_sys_clone')
    bpf.trace_print()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default=0)
    args = parser.parse_args()
    main(args.debug)
